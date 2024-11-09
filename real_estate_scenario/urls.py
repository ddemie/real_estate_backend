# real_estate_scenario/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('properties.urls')),  # Include the properties app URLs under /api/
]