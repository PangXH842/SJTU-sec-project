from django.shortcuts import render, HttpResponse
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
    loc_x = request.POST.get("x")
    loc_y = request.POST.get("y")
    desc = request.POST.get("description")
    LocationInfo.objects.create(name=name, loc_x=loc_x, loc_y=loc_y, description=desc)
    return redirect("http://127.0.0.1:8000/locations/list/")

def db_delete(request):
    nid = request.GET.get("nid")
    LocationInfo.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/locations/list/")