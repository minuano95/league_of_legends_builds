from django.contrib import admin
from .models import Champion, Classification, Category, Item, Build

# Register your models here.
admin.site.register(Champion)
admin.site.register(Classification)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Build)