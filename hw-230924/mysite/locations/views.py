from django.shortcuts import render, redirect, HttpResponse
from locations.models import LocationInfo

# Create your views here.
def index(request):
    return render(request, "index.html")

def locations_list(request):
    data_list = LocationInfo.objects.all()
    return render(request, 'locations_list.html', {"data": data_list})

def locations_add(request):
    if request.method == "GET":
        return render(request, 'locations_add.html')
    name = request.POST.get("name")
    x = request.POST.get("x")
    y = request.POST.get("y")
    description = request.POST.get("description")
    LocationInfo.objects.create(name=name, loc_x=x, loc_y=y, description=description)
    return redirect("http://127.0.0.1:8000/locations/list/")

def locations_delete(request):
    nid = request.GET.get("nid")
    LocationInfo.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/locations/list/")