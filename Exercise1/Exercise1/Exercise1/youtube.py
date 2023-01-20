# this is youtube navigator demo
from django.http import HttpResponse


def demo(request):
    return HttpResponse('<h1>Hello Panda</h1><br><p>this site for demo use below one is youtube navigator.</p><br><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Youtube</a>')
