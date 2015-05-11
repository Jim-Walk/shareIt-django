from django.shortcuts import render
from django.http import HttpResponse
from models import Image
from forms import ImageForm

def index(request):

    return render( request, 'index.html')

def images(request):
    contextdict = {}
    contextdict["images"] = Image.objects.all()
    return render(request, 'images.html', contextdict)

def uploadImage(request):

    if request.method== 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return images(request)
        else:
            print form.errors
    else:
        form = ImageForm()

    contextdict = {"form": form}
    return render(request, 'uploadImage.html', contextdict)


def about(request):

    return render(request, 'about.html')