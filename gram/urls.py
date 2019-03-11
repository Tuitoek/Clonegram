from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.landing,name = 'landing'),
    url('^home/',views.home2,name = 'home'),
    url('^profile/',views.profile,name = 'profile')
]
