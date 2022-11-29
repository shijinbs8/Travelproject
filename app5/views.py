from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import images


# Create your views here.
def index(request):
    obj = place.objects.all()
    img = images.objects.all()
    return render(request, 'index.html', {'theme': obj,'photo':img})
