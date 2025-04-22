from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
   
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_at = models.DateField(default=timezone.now)
    
    updated_at = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    
    
    def __str__(self):
        return self.dept_name
    
  
