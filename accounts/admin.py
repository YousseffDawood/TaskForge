from django.contrib import admin
from accounts.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'roles', 'is_staff', 'is_superuser')
    