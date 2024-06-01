
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
   
    path('', index, name='index'),
    path('blog/<slug:url>/', post, name='post'),
    path('category/<slug:url>/', category, name='category'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('terms/', term_and_condition, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('register/', user_signup, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='user_profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
