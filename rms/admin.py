from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id','name']
   list_per_page = 10
   search_fields = ['name']

class FoodAdmin(admin.ModelAdmin):
   list_display = ['id','name','category','price']
   list_per_page = 15
   search_fields = ['name']
   list_filter = ['category__name']

class TableAdmin(admin.ModelAdmin):
   list_display = ['id','name', 'capacity','is_available']

class OrderItemInline(admin.TabularInline):
   model = OrderItem

class OrderAdmin(admin.ModelAdmin):
   list_display = ['id','user','table','status','payment_status']
   list_per_page = 20
   search_fields = ['user__name', 'table__name']
   list_filter = ['status','payment_status']
   inlines = [OrderItemInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)

# postgresql download
# admin panel customize