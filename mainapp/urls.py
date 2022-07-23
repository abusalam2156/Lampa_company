from django.urls import path
from . import views,classesview

urlpatterns = [
    path('',views.home ,name="home" ),
    path('add',views.add ,name="add" ),
    path('delete/<int:id>/',views.delete ,name="delete" ),
    path('update/<int:id>/',views.update ,name="update" ),
    path('buy/<int:id>/',views.buy ,name="buy" ),
    path('display/<int:id>/',views.display ,name="display" ),
    path('search',views.search ,name="search" ),
  
     
    path('about',views.about ,name="about" ),
]