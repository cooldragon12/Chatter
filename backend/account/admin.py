from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'status',"public_key" ,'is_superuser')
    list_filter = ('status', 'is_superuser')
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()
    fieldsets = ()