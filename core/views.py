from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Faculte



def index(request):
    all_faculte = Faculte.objects.all()
    if request.method == "POST":
        faculte =  request.POST.get("faculte")
        departement = request.POST.get("departement")
        # Filtrer les facultés selon les criteres
        search_faculter = [
            n for n in all_faculte
            if str(n) == departement and n.faculte == faculte
        ]

        #Verifier si les resultats ont ete trouves
        if not search_faculter:
            message = "Pas de Resulta........................."
            context = {"message":message} 
            #------------return json
            return JsonResponse({"message": "Pas de Résulta trouvé"})
        else: 
            #Trier les resutats par semestre
            search_faculter_sorted = sorted(search_faculter, key=lambda x: x.semestre)
            context = {"results": search_faculter_sorted}
            results = [{"ue":n.ue, "semestre": n.semestre, "credit":n.credit} for n in search_faculter_sorted]
            #--------------Json 
            return JsonResponse({'results':results})
        #return render(request, 'index.html', context)

    return render(request,'index.html')
 
def docs(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        upload_file = request.FILES.get('upload_file')
        semestre = request.POST.get('semestre')

        if title and upload_file  and semestre:
            new_doc  = Doc.objects.create(title=title, file=upload_file, semestre=semestre)
            new_doc.save()
            
            return redirect('home')
    
    return render(request, "load.html")

def upload(request, pk):
    doc = get_object_or_404(Faculte, id=pk)
    file_path = doc.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(doc.file.name.split('/')[-1])
        return response



