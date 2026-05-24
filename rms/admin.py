from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']

class FoodAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category']
    list_filter=['category']
    search_fields=['name']
    list_per_page=10    
admin.site.register(Food,FoodAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display=['id','number','capacity','is_available']
    search_fields=['number','capacity','is_available']
admin.site.register(Table,TableAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields=['food']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','total_price','status','payment_status','user']
    list_filter=['status','payment_status']
    search_fields=['user_username']
    list_per_page=10 
    inlines=[OrderItemInline]
admin.site.register(Order,OrderAdmin)

# class OrderItemAdmin(admin.ModelAdmin):
#     list_display=['id','order','food']
#     list_filter=['order']
#     search_fields=['food_name']
#     list_per_page=10 
# admin.site.register(OrderItem,OrderItemAdmin)



