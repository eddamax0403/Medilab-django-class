
from django.contrib import admin
from django.urls import path
from medapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('starter/',views.starter,name='starter-page'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('department/',views.department,name='department'),
    path('doctor/',views.doctor,name='doctor'),
    path('contact/',views.contact,name='contact'),
    path('appoint/',views.appoint,name='appoint'),
    path('show/',views.show,name='show'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit,name='edit'),
]
