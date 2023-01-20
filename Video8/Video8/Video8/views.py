from django.http import HttpResponse

def index(request):
    return HttpResponse('Home<br><a href="http://127.0.0.1:8000/superman"><button>Next<button></a>')

def superman(request):
    return HttpResponse('Superman page <br><a href="http://127.0.0.1:8000/"><button>Back<button></a> <a href="http://127.0.0.1:8000/hulk"><button>Next<button></a>')

def hulk(request):
    return HttpResponse('Hulk page <br><a href="http://127.0.0.1:8000/superman"><button>Back<button></a> <a href="http://127.0.0.1:8000/batman"><button>Next<button></a>')

def batman(request):
    return HttpResponse('batman page <br><a href="http://127.0.0.1:8000/hulk"><button>Back<button></a> <a href="http://127.0.0.1:8000/spiderman"><button>Next<button></a>')


def spiderman(request):
    return HttpResponse('spiderman page <br><a href="http://127.0.0.1:8000/batman"><button>Back<button></a> <a href="http://127.0.0.1:8000/"><button>Home<button></a>')
