from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, category, add_rating

urlpatterns = [
    path('', home),
    path('blog/<slug:url>/', post),  # Added trailing slash
    path('category/<slug:url>/', category), 
    path('post/<slug:url>/', post, name='post'),  # Changed views.post to post
    path('post/<slug:url>/add_rating/', add_rating, name='add_rating'),  # Changed views.add_rating to add_rating
    path('category/<slug:url>/', category), # Added trailing slash
]

# Include static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
