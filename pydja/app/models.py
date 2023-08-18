from django.db import models

# Create your models here.

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="business")
    contactname = models.CharField(max_length = 50, default="business")
    address = models.CharField(max_length = 100, default="business")
    phone = models.CharField(max_length = 20, default="business")
    email = models.CharField(max_length = 50, default="business")
    country = models.CharField(max_length = 50, default="business")

    def __str__(self):
        return f"{self.companyname} from {self.country}"


class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "product")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"