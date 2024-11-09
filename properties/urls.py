# properties/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, ScenarioViewSet, ApplyScenarioViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'scenarios', ScenarioViewSet)

urlpatterns = router.urls + [
    path('apply-scenario/', ApplyScenarioViewSet.as_view(), name='apply-scenario')
]