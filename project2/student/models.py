from django.db import models
class pal(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=3,blank=True)
    email=models.EmailField(unique=True,blank=True)
    mobile=models.BigIntegerField()
    def __str__(self):
        return self.name
    
