from rest_framework import serializers
from .models import Property, Scenario, ScenarioImpact

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'latitude', 'longitude', 'address', 'base_value']


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'

class ScenarioImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioImpact
        fields = '__all__'