from django.conf.urls import include, url

from django.contrib import admin
from Register_Employer import views

admin.autodiscover()
urlpatterns = [
    url(r'accounts/', include('allauth.urls')),
    url(r'home/',views.emp_home),
    url(r'create/',views.register_employer),
]