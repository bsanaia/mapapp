from django.contrib import admin
from user.models import UserModel


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'address', 'country', 'phone']

admin.site.register(UserModel, UserAdmin)

