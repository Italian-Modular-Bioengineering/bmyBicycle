from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'frontend/home.html', locals())

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        print("Un upload has been requested")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        print ("this is the path:" + str(file_url))
        return render(request, 'frontend/upload.html', locals())
    return render(request, 'frontend/upload.html', locals())
