"""smnglofnet URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ------------------------------------------------
    # ADMIN
    path('admin/', admin.site.urls),

    # ------------------------------------------------
    # DJOSER
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),

    # ------------------------------------------------
    # APP AUTHS URL
    path('', include('auths.urls')),

    # ------------------------------------------------
    # USER FRIENDS
    path('', include('friends.urls')),
    path('friendship/', include('friendship.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
