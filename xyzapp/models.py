from pyexpat import model
from django.db import models


# Create your models here.
#Sales Data Model
class Sales(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    Region = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    ItemType = models.CharField(max_length=50)
    SalesChannel = models.CharField(max_length=100)
    OrderPriority = models.CharField(max_length=100)
    OrderDate = models.CharField(max_length=100)
    OrderID = models.CharField(max_length=100)
    ShipDate = models.CharField(max_length=100)
    UnitsSold = models.CharField(max_length=100)
    UnitPrice = models.CharField(max_length=100)
    UnitCost = models.CharField(max_length=100)
    TotalRevenue = models.CharField(max_length=100)
    TotalCost = models.CharField(max_length=100)
    TotalProfit = models.CharField(max_length=100)
    class Meta:
        db_table=("sales")

class Registration(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table=("registration") 