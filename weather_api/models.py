from django.db import models

DESCRIPTIONS = (
    (0, 'Sunny'),
    (1, "Rain"),
    (3, "Cloudy"),
    (4, "Snow")
)

class Description(models.Model):
    weather_description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    # will fix the data in descending order
    class Meta:
        ordering = ["-created_on"]

# py manage.py makemigrations weather_api