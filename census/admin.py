from django.contrib import admin

# Register your models here.

from .models import State
from .models import District
from .models import City
from .models import Village

admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Village)

