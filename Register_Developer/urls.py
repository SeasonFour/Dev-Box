from django.conf.urls import include, url
from Register_Developer import views
urlpatterns = [
    url(r'me/',views.profile),

    url(r'edit/',views.edit_profile),
    url(r'new/portfolio$',views.new_portfolio),

    url(r'create/$',views.create_profile),
    url(r'create/portfolio/$',views.create_portfolio),
]
