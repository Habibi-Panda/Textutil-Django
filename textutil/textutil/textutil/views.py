# I have Created this file - Panda
from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/about'>Hello Panda</a>")

def about(request):
    return HttpResponse("This is About Page")