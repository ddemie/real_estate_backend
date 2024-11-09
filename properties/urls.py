# properties/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.get_properties, name='get_properties'),
    path('scenarios/', views.get_scenarios, name='get_scenarios'),
    path('properties/<int:property_id>/apply-scenario/<int:scenario_id>/', views.apply_scenario_to_property, name='apply_scenario'),
]