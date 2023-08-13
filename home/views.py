from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners as ps



def index(request):
    shorten_url='NA'
    try:
        if request.method=="POST":
            url=request.POST.get("website-link")
            s = ps.Shortener()
            shorten_url=s.tinyurl.short(url)
    except:
        return HttpResponse("Some Error Occured");
    return render(request, 'index.html',{"link":shorten_url})
