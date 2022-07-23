from django import forms
from . import models 
class addform(forms.ModelForm):
   class Meta:
        fields = "__all__"
        exclude = ['adder']
        model = models.products
