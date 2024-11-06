"""
URL configuration for kirro_dep_dashboard project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", admin.site.urls),
    path('supabase-queries/', include('api.urls')),
    path('', include('django.contrib.auth.urls')), 
]
