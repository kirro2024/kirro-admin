"""
URL configuration for kirro_dep_dashboard project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('supabase-query/', include('api.urls')),
    path("", admin.site.urls), 
]
