from . import views
from django.urls import path


urlpatters = [

   path('', views.home, name='home'),
   path('admin/',  views.admin.site.urls),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),


]


