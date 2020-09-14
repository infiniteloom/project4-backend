from django.db import models
from django import forms
from apps.authentication.models import User

INT_CHOICES = [tuple([x,x]) for x in range(1,10)]





# Create your models here.
class Realtor(User):

    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.IntField(max_length=5)
    company = models.CharField(max_length=100)
    listings = models.ManyToManyField('Listing')

    def __str__(self):
        return self.name


#### Buyer Model
class Buyer(User):

    favorites = models.ManyToManyField('Listing')

    def __str__(self):
        return self.name

#### Listing Model
class Listing(models.Model):
    type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.IntegerField(max_length=5)
    street = models.CharField(max_length=100)
    year_built = models.IntegerField(max_length=4)
    bed = models.IntegerField(max_length=2)
    bath = models.IntegerField(max_length=2)
    home_size = models.IntegerField(max_length=7) #square feet
    lot_size = models.IntegerField(max_length=7)  # acres
    price = models.IntegerField(max_length=10)
    description = models.TextField()
    images = models.TextField()

    created_at= models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)

    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

