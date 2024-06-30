from django.shortcuts import render, redirect
from .models import Doc


def index(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        upload_file = request.FILE.get('upload_file')
        semestre = request.POST.get('semestre')

        if title and upload_file  and semestre:
            new_doc  = Doc.objects.create(tilte=title, file=upload_file, semestre=semestre)
            new_doc.save()
            return redirect('home')
        else:
            erro_message = "Veuille remplire bien les champs"
    
    else:
        erro_message = "None"

            
    
    return render(request, "index.html", {"message": erro_message})

