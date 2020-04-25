from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('base_layout',views.base_layout,name='base_layout'),
    path('getdata',views.getdata,name='getdata'),
    path('remove/<id>',views.remove,name='remove'),
    path('edit/<id>',views.edit,name='edit'),
] 
