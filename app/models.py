from django.db import models
import uuid

class signup(models.Model):
    nam=models.CharField(max_length=30)
    numb=models.IntegerField()
    ema=models.EmailField()
    pwd=models.CharField(max_length=30)

    def __str__(self):
        return self.na

class Categories(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
  
class Products(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    pid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    des=models.CharField(max_length=500)
    img=models.ImageField(upload_to='images/')
    offer=models.CharField(max_length=500)
    price=models.FloatField()

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(signup,on_delete=models.CASCADE)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    order_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    quantity=models.PositiveBigIntegerField(default=0)
    total=models.PositiveBigIntegerField(default=0)


