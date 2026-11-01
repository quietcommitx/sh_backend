from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
   fieldsets = (
      (None, {"fields": ("username", "password")}),
      (("Personal info"), {"fields": ("first_name", "last_name", "phone","email")}),
      (
         ("Permissions"),
         {
            "fields": (
               "is_active",
               "is_staff",
               "is_superuser",
               "groups",
               "user_permissions",
            ),
         },
      ),
      (("Important dates"), {"fields": ("last_login", "date_joined")}),
   )
   list_display = ['username','email','phone']

admin.site.register(User, CustomUserAdmin)