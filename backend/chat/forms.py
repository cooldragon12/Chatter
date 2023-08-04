
from django import forms
from django.contrib.auth.models import Permission
from .models import Room
from account.models import User

from django.forms.widgets import CheckboxSelectMultiple
class RoomAdminForm(forms.ModelForm):
    # groups = forms.MultipleChoiceField()
    class Meta:
        model = Room
        fields = ("name","host", 'max_users','members')
        
    def __init__(self, *args, **kwargs):
        
        super(RoomAdminForm, self).__init__(*args, **kwargs)
        
        self.fields["members"].widget = CheckboxSelectMultiple()
        self.fields["members"].queryset = User.objects.all()