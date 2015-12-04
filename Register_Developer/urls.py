from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'me/',views.profile),
    url(r'edit/$',views.edit),
    url(r'create/$',views.create),
]