from django.db import models
from apps.authentication.models import User

"""
# Create your models here.
class RealtorUser(User):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.IntegerField()
    company = models.CharField(max_length=100)

    #listings = models.OneToManyField('Listing') ########################

    def __str__(self):
        return self.first_name + " " + self.last_name





#### Buyer Model
class BuyerUser(User):  ########### INHERITANCE?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #favorites = models.ManyToManyField('Listing') #####################

    def __str__(self):
        return self.first_name + " " + self.last_name

"""


#### Listing Model
class Listing(models.Model):
    type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()
    street = models.CharField(max_length=100)
    year_built = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    home_size = models.IntegerField() #square feet
    lot_size = models.FloatField()  # acres
    price = models.IntegerField()
    description = models.TextField()
    image1 = models.TextField(default=None)
    image2 = models.TextField(default=None)
    image3 = models.TextField(default=None)
    image4 = models.TextField(default=None)
    interested_buyers = models.ManyToManyField(User, related_name='interested_buyers')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    realtor = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.street + ", " + self.city + ", " + self.state + ", " + self.zip

