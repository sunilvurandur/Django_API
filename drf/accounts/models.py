from django.db import models

# Create your models here.

class advisors(models.Model):
    Advisor_Name=models.CharField(max_length=30)
    Advisor_Photo=models.CharField(max_length=50)
    def __str__(self):
        return self.Advisor_Name
    
class booking(models.Model):
    booking_time=models.DateTimeField()