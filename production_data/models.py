from django.db import models

class GasField(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    discovery_date = models.DateField(null=True, blank=True)
    total_area = models.FloatField(null=True, blank=True, help_text="Area in square kilometers")
    
    def __str__(self):
        return self.name
    
    def get_total_production(self):
        """Returns total gas production across all wells in the field"""
        return sum(
            well.production_data.aggregate(models.Sum('flow_rate'))['flow_rate__sum'] or 0
            for well in self.wells.all()
        )
# Update the Well model to make gas_field required
class Well(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    gas_field = models.ForeignKey(
        GasField,
        on_delete=models.CASCADE,
        related_name='wells'
    )
    
    def __str__(self):
        return self.name

class ProductionData(models.Model):
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name='production_data')
    date = models.DateField()
    flow_rate = models.FloatField()
    cumulative_flow_rate = models.FloatField()
    water_production = models.FloatField()
    condensate_production = models.FloatField()
    
    class Meta:
        ordering = ['date']
        unique_together = ['well', 'date']
        
    def __str__(self):
        return f"{self.well.name} - {self.date}"