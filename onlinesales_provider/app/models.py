from django.db import models

# Create your models here.
class merchantModel(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class ProductModel(models.Model):
    p_no = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50,unique=True)
    p_price = models.FloatField()
    p_qunt = models.IntegerField()
    p_type = models.ForeignKey(merchantModel,on_delete=models.CASCADE)
