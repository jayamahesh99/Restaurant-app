from django.db import models

# Create your models here.
class product(models.Model):

    Title=models.CharField(max_length=100)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')


