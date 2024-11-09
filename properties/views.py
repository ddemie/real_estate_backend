# properties/views.py

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Property, Scenario, ScenarioImpact
from .serializers import PropertySerializer, ScenarioSerializer, ScenarioImpactSerializer

class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# Property ViewSet
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# Scenario ViewSet
class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

# Apply Scenario View
class ApplyScenarioViewSet(APIView):
    def post(self, request, *args, **kwargs):
        property_id = request.data.get("property_id")
        scenario_id = request.data.get("scenario_id")

        try:
            property_obj = Property.objects.get(id=property_id)
            scenario_obj = Scenario.objects.get(id=scenario_id)
            adjusted_value = property_obj.base_value * (1 + (scenario_obj.impact_factor / 100))

            impact = ScenarioImpact.objects.create(
                property=property_obj,
                scenario=scenario_obj,
                adjusted_value=adjusted_value
            )
            return Response(ScenarioImpactSerializer(impact).data)
        except Property.DoesNotExist:
            return Response({"error": "Property not found"}, status=404)
        except Scenario.DoesNotExist:
            return Response({"error": "Scenario not found"}, status=404)