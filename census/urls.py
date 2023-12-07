from django.urls import path

from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("states/", views.state_list, name="state_list"),
    path("states/<int:state_id>/", views.district_list, name="district_list"),
    path("districts/<int:district_id>/", views.city_list, name="city_list"),
    path("cities/<int:city_id>/", views.village_list, name="village_list"),
    path("districts/", views.district, name="district"),
    path("villages/", views.village, name="village"),
    path("cities/", views.cities, name="cities"),
    path("village/<int:village_id>/", views.village_info, name="village_info"),
    path('get_location/', views.get_location, name="get_location"),
    path('search/', views.search, name="search")
]


