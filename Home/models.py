from django.db import models

# Create your models here.
class Contact(models.Model):
    # id=models.IntegerField(primary_key=True,auto_created=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=12,unique=True)
    date=models.DateField()
    extra=models.CharField(max_length=100)
    def __str__(self):
        return self.first_name