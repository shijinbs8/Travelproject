from django.contrib import admin

# Register your models here.
from . models import place
from . models import images

admin.site.register(place)
admin.site.register(images)
