from django import forms
from .models import Menu, Booking

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('title', 'price', 'inventory')
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'guests', 'date')