from django.contrib import admin
from user.models import UserModel, ProfileModel


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'address', 'country', 'phone']

admin.site.register(UserModel, UserAdmin)
admin.site.register(ProfileModel)
