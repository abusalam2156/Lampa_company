from django.urls import path
from .forms import sendpasswordmail 
from . import views
from django.contrib.auth import views as passsview
urlpatterns = [


   path('login',views.userlogin ,name="login" ),            # login user and show welcome user at home page
   path('logout',views.userlogout ,name="logout" ),            # login user and show welcome user at home page
   path('register',views.register ,name="register" ),   ## save name and mail and password of user
   path('logout',views.logout ,name="logout" ),       # logout the user name
  
 path('password_reset',passsview.PasswordResetView.as_view(form_class=sendpasswordmail),name="pass_reset" ),    # logout the user name
   path('password_reset/done',passsview.PasswordResetDoneView.as_view(template_name='password_reset_done.html') ,name="password_reset_done" ),    # logout the user name
   path('password_reset/confirm<uidb64>/<token>/',passsview.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html') ,name="password_reset_confirm" ),    # logout the user name
    path('password_reset/complete',passsview.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete" ),    # logout the user name

 
]