from django.forms import ModelForm
from .models import Hero

# Create the form class.
class HeroForm(ModelForm):
     class Meta:
         model = Hero
         fields = [ 'name', 'alias']