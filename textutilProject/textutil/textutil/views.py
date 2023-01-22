from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzer(request):
    text= request.GET.get('textarea')
    print(text)
    removepunc =request.GET.get('removepunc','off')
    uppercase =request.GET.get('uppercase','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    print(removepunc)
    if removepunc == "on":
        analyze=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in text:
            if char not in punctuations:
                analyze = analyze + char
        params = {"purpuse":"Remove Punctuations","analyze":analyze}
        # return render(request,"analyzer.html",params)

    if(uppercase == "on"):
        analyze=""
        for char in text:
            analyze = analyze + char.upper()
        params = {"purpuse":"Change Text into Uppercase","analyze":analyze}
        # return render(request,"analyzer.html",params)
        text = analyze

    if(newlineremover == "on"):
        analyze=""
        for char in text:
            if char != '\n':
                analyze = analyze + char
        params = {"purpuse":"Remove New Line","analyze":analyze}
        # return render(request,"analyzer.html",params)
        text = analyze

    if(extraspaceremover == "on"):
        analyze=""
        for i, char in enumerate(text):
            if not(text[i]==" " and text[i+1] =="  "):
                analyze = analyze + char
        params = {"purpuse":"Remove Extra Space","analyze":analyze}
        # return render(request,"analyzer.html",params)
        text = analyze

    if (charcount == "on"):
        analyze = 0
        for i in range(0,len(text)):
            if text[i] != "":
                analyze=analyze+1
        params = {"purpuse": "Remove Extra Space", "analyze": analyze}
        # return render(request, "analyzer.html", params)
        text = analyze

    if (removepunc != "on" and uppercase != "on" and newlineremover != "on" and charcount != "on"):
        return HttpResponse('Please enter your value')
        
    return render(request,"analyzer.html",params)
    # merge=text+'<br>'+removepunc
    # return HttpResponse(merge)

# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")


# def charcount(request):
#     return HttpResponse("charcount")
