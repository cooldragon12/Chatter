

from django.contrib import admin
from .models import Message, Room
from .forms import RoomAdminForm
# Register your models here.

@admin.register(Message)
class MessageAdminView(admin.ModelAdmin):
    list_display = ("id","conversation", "user", "timestamp")
    list_filter = ("conversation", "user")
    search_fields = ("conversation", "user")
    readonly_fields = ("timestamp",)
    ordering = ("timestamp",)
@admin.register(Room)
class RoomAdminView(admin.ModelAdmin):
    list_display = ("id","name", "max_users", "code", 'search_id')
    form = RoomAdminForm

