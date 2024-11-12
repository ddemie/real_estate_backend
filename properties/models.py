# models.py
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    base_value = models.DecimalField(max_digits=15, decimal_places=2, default=1000000)
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Scenario(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    impact_factor = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text="Impact factor as a percentage increase or decrease (e.g., 5.00 for +5%)"
    )
    
    def __str__(self):
        return self.name

class ScenarioImpact(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    adjusted_value = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"{self.property} under {self.scenario}"