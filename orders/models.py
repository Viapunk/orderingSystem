from django.db import models
from enumfields import EnumField
from enumfields import Enum

# Create your models here.

class PRIVILEDGE(Enum):
    CLIENT = 'Client',
    EMPLOYEE = 'Employee',
    ADMIN = 'Admin'

class STATUS(Enum):
    DURING_COMPLETION = 'DuringCompletion',
    READY_TO_COLLECT = 'ReadyToCollect',
    COLLECTED = 'Collected'

class PAYMENT(Enum):
    CARD = 'Card',
    CASH = 'Cash'

class Person(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=40, blank=True)
    priviledge = EnumField(PRIVILEDGE, max_length=1)

class Product_category(models.Model):
    name = models.CharField(max_length=70, blank=False)
    representingImage = models.ImageField(blank=False)

class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    quantity = models.IntegerField(blank=False)
    image = models.ImageField(blank=False)
    category = models.OneToOneField(Product_category, on_delete=models.CASCADE, primary_key=True)

    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset


class Order(models.Model):
    productList = models.ForeignKey(Product, on_delete=models.PROTECT)
    isAssigned = models.BooleanField(default=False,blank=False)
    assignee = models.ForeignKey(Person, blank=True, on_delete=models.PROTECT)
    status = EnumField(STATUS, default=STATUS.DURING_COMPLETION, blank=False)
    paymentMethod = EnumField(STATUS, default=PAYMENT.CASH, blank=False)
