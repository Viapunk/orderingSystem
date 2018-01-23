from django.db import models
from enumfields import EnumField
from enumfields import Enum

# Create your models here.

class PRIVILEDGE(Enum):
    CLIENT = 'Client',
    EMPLOYEE = 'Employee',
    ADMIN = 'Admin'

class STATUS(Enum):
    COMPLETING = 'Completing',
    READY = 'Ready',
    COLLECTED = 'Collected'

class PAYMENT(Enum):
    CARD = 'Card',
    CASH = 'Cash'

class Person(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=40, blank=True)
    priviledge = EnumField(PRIVILEDGE, max_length=10)

    def __str__(self):
        return self.firstName + " " + self.lastName;

class Product_category(models.Model):
    name = models.CharField(max_length=70, blank=False, default="Product")
    image = models.ImageField(upload_to='media', default="")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    image = models.ImageField(upload_to='media', default="")
    category = models.ForeignKey(Product_category, on_delete=models.CASCADE)

    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset

    def __str__(self):
        return self.name

class Order(models.Model):
    productList = models.ForeignKey(Product, on_delete=models.PROTECT)
    isAssigned = models.BooleanField(default=False,blank=False)
    assignee = models.ForeignKey(Person, blank=True, on_delete=models.PROTECT)
    status = EnumField(STATUS, default=STATUS.COMPLETING, blank=False)
    #paymentMethod = EnumField(PAYMENT, default="Cash", blank=False, max_length=10)

    def __str__(self):
        return self.id + " " + self.status
