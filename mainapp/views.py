from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models,forms
from django.contrib.auth.decorators import login_required
def home(request):    
    product=models.products.objects.all() 
    data={'products':product}
    return render(request,'home.html',data)

def add(request):
    form=forms.addform()
  
    if (request.method=='POST'):
    
        form=forms.addform(request.POST,request.FILES)             
        
        if form.is_valid():
      
                 username=request.user
                 name=form.cleaned_data ["name"]
                 brief=form.cleaned_data["brief"]
                 image=form.cleaned_data["image"]
                 price=form.cleaned_data["price"]
                 
                 new_add=models.products(adder=username,name=name,brief=brief,image=image,price=price)
                 last_add=models.products.objects.last()
                 if models.products.objects.all().count()==0:
                      new_add.save()
                 elif (last_add.name != new_add.name):
                      new_add.save()
                 
                 if 'gohome' in request.POST:
                     messages.success(request, ' added successfully')
                     return HttpResponseRedirect('/') 

                 elif'addother' in request.POST:
                     data={'form':form}
                     messages.success(request, ' added successfully')
                     return render(request, 'add.html',data)
               
   
   
    data={'form':form}
    return render(request, 'add.html',data)
def update(request,id):
    p=models.products.objects.get(id=id)   
    init_data = {
     'name': p.name,
     'brief': p.brief,
     'image': p.image,
     'price': p.price
      }
    form=forms.addform(initial=init_data)
  
    if (request.method=='POST'):
    
        form=forms.addform(request.POST,request.FILES)             
        
        if form.is_valid():
                 p=models.products.objects.get(id=id)
                 p.adder=request.user
                 p.name=form.cleaned_data ["name"]
                 p.brief=form.cleaned_data["brief"]
                 p.image=form.cleaned_data["image"]
                 p.price=form.cleaned_data["price"]
                 p.save()
                 messages.success(request, ' updated successfully')
                 return HttpResponseRedirect('/') 
    
    data={'form':form}
    return render(request, 'update.html',data)
   
   
    return render(request, 'update.html')
def delete(request,id):
    if (request.method=='POST') and  'keep' in request.POST:
        return HttpResponseRedirect('/') 
    elif (request.method=='POST') and  'delete' in request.POST:
        models.products.objects.get(id=id).delete()
    
        messages.error(request, ' deleted successfully')
        return HttpResponseRedirect('/') 
    
    return render(request, 'delete.html')
def display(request,id):
    p=models.products.objects.get(id=id)
    c=models.comments.objects.filter(product=p)
    data={'p':p,
           'comments':c}
    if (request.method=='POST'):
        if 'del' in request.POST :
                
                id1=int(request.POST.get("del"))
                models.comments.objects.get(id=id1).delete()
        elif 'add' in request.POST:
                
                comment=models.comments()
             
                comment.text=request.POST.get("text")
                comment.product=models.products.objects.get(id=id)
                comment.adder=request.user
                if(comment.text!=''):comment.save()
        return HttpResponseRedirect(request.path_info)
    
     
    return render(request, 'display.html',data)
def search(request):
    if (request.method=='POST'):
        name = request.POST.get("name")
        product=models.products.objects.filter(name__icontains=name) 
        data={'products':product}
        return render(request,'search.html',data)
    return render(request, 'search.html')
@login_required()
def buy(request,id):
    data={'p':models.products.objects.get(id=id)}
    return render(request, 'buy.html',data)

def about(request):
    return render(request, 'about.html')
