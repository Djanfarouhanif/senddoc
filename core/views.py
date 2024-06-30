from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Doc


def index(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        upload_file = request.FILES.get('upload_file')
        semestre = request.POST.get('semestre')

        if title and upload_file  and semestre:
            new_doc  = Doc.objects.create(title=title, file=upload_file, semestre=semestre)
            new_doc.save()
            print("**********************")
            return redirect('home')
        else:
            erro_message = "Veuille remplire bien les champs"
    
    else:
        erro_message = "None"

            
    
    return render(request, "index.html", {"message": erro_message})

def upload(request, pk):
    doc = get_object_or_404(Doc, id=pk)
    

    file_path = doc.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(doc.file.name.split('/')[-1])
        return response


def docs(request):
    all_doc = Doc.objects.all()

    return render(request, 'index.html', {"docs":all_doc})
