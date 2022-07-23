from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
def userlogin(request):
    if (request.method=="POST"):
             postname=request.POST.get('name')
             postpass=request.POST.get('password')
             user=authenticate(username=postname,password=postpass)
             if user:     #if is exist in users database 
                 nxt=request.GET.get('next', '')
                 login(request,user)
                 messages.success(request, f'welcome {postname}')
                 return HttpResponseRedirect(nxt)
    
             else:
                
                  isgoodname=User.objects.filter(username=postname)
                  return render(request, 'login.html',
                        {
                          'postedname':postname,
                          'isgoodname':isgoodname,
                          
                          
                        })
       
    else:
       
         return render(request, 'login.html',{'mm':'llllll'})                        
def register(request):
          if (request.method=="POST"):
    
                      name=request.POST.get('name')
                      email=request.POST.get('email')
                      password=request.POST.get('password')
                      dataname= User.objects.filter(username=name).first()
                      datamail= User.objects.filter(email=email).first()
                      
                      if dataname :
                         return render(request, 'register.html',{'nameexist': name})
                      else:
                        
                        User.objects.create_user(username=name,email=email,password=password)
                        user=authenticate(username=name,password=password)
                        login(request=request,user=user)
                        messages.success(request, f'successfuly acount created for {name}')
                        return HttpResponseRedirect('/')
  

          else:
            return render(request, 'register.html')    
def userlogout(request):
   logout(request)
   return render(request, 'logout.html')   
