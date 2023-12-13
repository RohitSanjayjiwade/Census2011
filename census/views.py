from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import State, District, City, Village
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    return render(request, "states/index.html")

def state_list(request):
    state_list = State.objects.all() 
    return render(request, "states/states.html", {"state_list": state_list})

def district_list(request, slug):
    state = get_object_or_404(State, slug=slug)
    return render(request, "states/detail.html", {"state": state})


def city_list(request, slug):
    district = get_object_or_404(District, slug=slug)
    return render(request, "states/cities.html",{"district": district})

def district(request):
    district_list = District.objects.all()

    # Number of items to display per page
    items_per_page = 2
    paginator = Paginator(district_list, items_per_page)
    page = request.GET.get('page')

    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results.
        paginated_data = paginator.page(paginator.num_pages)

    return render(request, "states/district.html",{"district_list": district_list})

def village_list(request, slug):
    city = get_object_or_404(City, slug=slug)

    items_per_page = 10
    paginator = Paginator(city.village_set.all(), items_per_page)
    page = request.GET.get('page')

    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results.
        paginated_data = paginator.page(paginator.num_pages)
    return render(request, "states/villages.html",{"city": city, "villages_list": paginated_data})

def village(request):
    villages_list = Village.objects.all()

    # Number of items to display per page
    items_per_page = 10
    paginator = Paginator(villages_list, items_per_page)
    page = request.GET.get('page')

    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results.
        paginated_data = paginator.page(paginator.num_pages)

    return render(request, "states/village_list.html",{"villages_list": paginated_data})

def cities(request):
    cities = City.objects.all()

    # Number of items to display per page
    items_per_page = 10
    paginator = Paginator(cities, items_per_page)
    page = request.GET.get('page')

    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results.
        paginated_data = paginator.page(paginator.num_pages)

    return render(request, "states/cities_list.html",{"cities_list": paginated_data})

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
