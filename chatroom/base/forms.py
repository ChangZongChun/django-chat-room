from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # the item you want to show from the model(Room)
        fields = '__all__'