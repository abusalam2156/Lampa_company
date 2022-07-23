from django.views import generic
from . import models
from django.shortcuts import get_list_or_404, get_object_or_404
class add(generic.CreateView):
    template_name='add.html'
    model=models.products
    fields=['image','name','brief','price'] 
    success_url = '/'

  