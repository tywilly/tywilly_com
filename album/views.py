from django.shortcuts import render

from album.models import Photo
# Create your views here.
def index(request):

    context = {
        'photos': Photo.objects.all()
    }

    return render(request, "album/index.html", context=context)