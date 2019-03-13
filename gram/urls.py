from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views as core_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url('^$', views.landing, name='landing'),
    url('^home/', views.home2, name='home'),
    url('^profile/', views.profile, name='profile'),
    url('^search/', views.searchresults, name='searchresults'),
    url('^register/', views.register, name='register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url('^accounts/login/$', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(
        template_name='registration/logout.html'), name='logout'),
    url(r'^comments/', views.comments, name="comments"),
    url(r'^admin/$', views.test_redirect, name='test_redirect'),
    url('^profile/editprofile/',    views.profile_form, name='profile_form'),
    url(r'^friendship/', include('friendship.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
