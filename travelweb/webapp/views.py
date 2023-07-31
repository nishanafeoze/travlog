from django.shortcuts import render
from .models import place, TeamMember

from django.http import HttpResponse

def demo(request):
    return render(request,"demo.html")
def index(request):
    obj=place.objects.all()
    obj1 = TeamMember.objects.all()
    return render(request, "index.html", {'result': obj,'team':obj1})





# Create your views here.
