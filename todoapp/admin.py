from django.contrib import admin

# Register your models here.
from .models import ListItem,List
admin.site.register(ListItem)
admin.site.register(List)