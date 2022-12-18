from django.contrib import admin
from .models import Products, Order

#To make customisations to admin panel
admin.site.site_header="E-Commerce Site"
admin.site.site_title="Fashion Shopping"

admin.site.index_title="Manage Fahion Shopping"

#If we want to display additional fields apart from title field as well use class and name it as modelnameAdmin and register this class with admin like we register models
class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
        
    change_category_to_default.short_description="Default Category"
    list_display=('title',' price','discount_price','category','image')
    #we can search the data in admin panel using below fields
    search_fields=('title','category')
    actions=('change_category_to_default')
    fields=('title','price')
    list_editable=('price','category')
# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)