# serializers.py
from rest_framework import serializers
from .models import Property, Scenario, ScenarioImpact

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'address', 'price', 'description', 'latitude', 'longitude']


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'

class ScenarioImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioImpact
        fields = '__all__'