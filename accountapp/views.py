from django.shortcuts import render

from .models import Video

# Create your views here.
from django.views.generic import ListView


def start(request):
    return render(request, 'accountapp/index.html')

def test(request):
    return render(request, 'accountapp/test.html')

def upload(request):
    if request.method == 'post':
        upload_file = request.FiLES['video']
    return render(request, 'accountapp/modals.html')


