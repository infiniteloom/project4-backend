from django.db import models
from django import forms

INT_CHOICES = [tuple([x,x]) for x in range(1,10)]

# Create your models here.
class Realtor(models.Model):
    region = forms.ChoiceField[
        ('')
    ]
    city = models.CharField(max_length=100),
    zip = models.IntField(max_length=10),
    name = models.CharField(max_length=100),
    company = models.CharField(max_length=100),
    listings = models.ManyToManyField('Listing')

    def __str__(self):
        return self.name


#### Buyer Model
class Buyer(models.Model):
    name = models.CharField(max_length=100),
    email = models.CharField(max_length=100),
    favorites = models.ManyToManyField('Listing')

    def __str__(self):
        return self.name

#### Listing Model
class Listing(models.Model):
    type = dropdown menu,
    city = models.CharField(max_length=100),
    state = drop down menu, 2 letters,
    zip = models.IntegerField(max_length=10),
    street = models.CharField(max_length=100),
    year_built = models.IntegerField(max_length=4),
    bed = drop down menu could be cool,
    bath = drop down menu,
    home_size = models.IntegerField(max_length=7), #square feet
    lot_size = models.IntegerField(max_length=7),  # acres
    price =  models.IntegerField(max_length=10),
    description = models.TextField(),
    images = models.TextField(),
    created_by = models.ForeignKey(Realtor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

