from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('courses/',views.courses, name='courses'),
]