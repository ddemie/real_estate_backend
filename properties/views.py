# properties/views.py

import json
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Property, Scenario, ScenarioImpact
from .serializers import PropertySerializer, ScenarioSerializer, ScenarioImpactSerializer
from rest_framework import status
from rest_framework.decorators import api_view



# update property description
def update_property_description(request, property_id):
    if request.method == 'PATCH':
        property_obj = get_object_or_404(Property, id=property_id)
        
        # Parse JSON data
        data = json.loads(request.body)
        new_description = data.get("description")

        if new_description:
            property_obj.description = new_description
            property_obj.save()
            return JsonResponse({"success": True, "description": property_obj.description})
        else:
            return JsonResponse({"error": "Description not provided."}, status=400)
    
    return JsonResponse({"error": "Only PATCH method is allowed."}, status=405)


# New view to get a single property by its ID
def get_property_by_id(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    serializer = PropertySerializer(property_obj)
    return JsonResponse(serializer.data)


# GET /api/properties
def get_properties(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return JsonResponse(serializer.data, safe=False)


# GET /api/scenarios
def get_scenarios(request):
    scenarios = Scenario.objects.all()
    serializer = ScenarioSerializer(scenarios, many=True)
    return JsonResponse(serializer.data, safe=False)


# POST /api/properties/{propertyId}/apply-scenario/{scenarioId}
def apply_scenario_to_property(request, property_id, scenario_id):
    # Retrieve the property and scenario, or return a 404 error if not found
    property_obj = get_object_or_404(Property, id=property_id)
    scenario_obj = get_object_or_404(Scenario, id=scenario_id)

    # Calculate the adjusted value
    adjusted_value = property_obj.price * scenario_obj.adjustment_factor

    # For demonstration purposes, return the calculated result directly
    result = {
        'property_id': property_id,
        'scenario_id': scenario_id,
        'adjusted_value': adjusted_value
    }
    return JsonResponse(result)


# Property ViewSet
class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


# Scenario ViewSet
class ScenarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


# Apply Scenario API View for applying a scenario to a property
class ApplyScenarioViewSet(APIView):
    def post(self, request, *args, **kwargs):
        property_id = request.data.get("property_id")
        scenario_id = request.data.get("scenario_id")

        # Fetch the property and scenario objects, or return 404 if not found
        property_obj = get_object_or_404(Property, id=property_id)
        scenario_obj = get_object_or_404(Scenario, id=scenario_id)

        # Calculate the adjusted value
        adjusted_value = property_obj.price * (1 + (scenario_obj.adjustment_factor / 100))

        # Save the impact record
        impact = ScenarioImpact.objects.create(
            property=property_obj,
            scenario=scenario_obj,
            adjusted_value=adjusted_value
        )

        # Return the serialized impact data
        return Response(ScenarioImpactSerializer(impact).data)