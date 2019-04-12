from django.contrib import admin
from .models import Shop, Item

#admin.site.register(Shop)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Item)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'name_length', 'address']
