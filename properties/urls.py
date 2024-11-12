# properties/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.get_properties, name='get_properties'),
    path('properties/<int:property_id>/', views.get_property_by_id, name='get_property_by_id'),  # New endpoint
    path('scenarios/', views.get_scenarios, name='get_scenarios'),
    path('properties/<int:property_id>/apply-scenario/<int:scenario_id>/', views.apply_scenario_to_property, name='apply_scenario'),
    path('properties/<int:property_id>/update-description/', views.update_property_description, name='update_property_description')
]