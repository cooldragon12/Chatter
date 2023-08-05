

from django.contrib import admin
from .models import Message, User, Room
from .forms import RoomAdminForm
# Register your models here.

admin.site.register(Message)

@admin.register(Room)
class RoomAdminView(admin.ModelAdmin):
    list_display = ("id","name", "max_users", "code", 'search_id')
    form = RoomAdminForm
