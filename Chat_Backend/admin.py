

from django.contrib import admin
from .models import User, Room
from .forms import RoomAdminForm
# Register your models here.

admin.site.register(User)
@admin.register(Room)
class RoomAdminView(admin.ModelAdmin):
    list_display = ("name", "max_users", "code", 'search_id')
    form = RoomAdminForm

