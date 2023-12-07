from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import State, District, City, Village
# Create your views here.

def index(request):
    return render(request, "states/index.html")

def state_list(request):
    state_list = State.objects.all() 
    return render(request, "states/states.html", {"state_list": state_list})

def district_list(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    return render(request, "states/detail.html", {"state": state})


def city_list(request, district_id):
    district = get_object_or_404(District, pk=district_id)
    return render(request, "states/cities.html",{"district": district})

def district(request):
    district_list = District.objects.all()
    return render(request, "states/district.html",{"district_list": district_list})

def village_list(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, "states/villages.html",{"city": city})

def village(request):
    villages_list = Village.objects.all()
    return render(request, "states/village_list.html",{"villages_list": villages_list})

def cities(request):
    cities = City.objects.all()
    return render(request, "states/cities_list.html",{"cities_list": cities})

def village_info(request, village_id):
    village_info = get_object_or_404(Village, pk=village_id)
    return render(request, "states/villageInfo.html",{"village": village_info})

def get_location(request):
    village_data = None

    if request.method == 'POST':
        pincode = request.POST.get('pincode')

        if pincode:
            try:
                village_data = Village.objects.filter(pincode = pincode)
            except:
                print("no found")
                village_data = None

        return render(request, "states/search.html", {"village_data": village_data, "pincode_value": pincode})




def search(request):
    return render(request, "states/search_form.html")


def pincode(request, pincode):
    try:
        village_data = Village.objects.filter(pincode = pincode)
    except:
        print("no found")
        village_data = None
    return render(request, "states/search.html", {"village_data": village_data, "pincode_value": pincode})
