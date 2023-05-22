from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'phone', 'role', 'image',)
    readonly_fields = ('last_login', 'image',)
    filter_horizontal = ()
    list_filter = ('role', 'email')
    list_per_page = 10
    list_max_show_all = 100
