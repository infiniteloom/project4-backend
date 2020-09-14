from django.db import models
from apps.authentication.models import User


# Create your models here.
class RealtorUser(User):

    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.IntegerField()
    company = models.CharField(max_length=100)

    listings = models.ManyToManyField('Listing')

    def __str__(self):
        return self.first_name + " " + self.last_name





#### Buyer Model
class BuyerUser(User):

    favorites = models.ManyToManyField('Listing')

    def __str__(self):
        return self.first_name + " " + self.last_name




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
    lot_size = models.IntegerField()  # acres
    price = models.IntegerField()
    description = models.TextField()
    images = models.TextField()

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)

    realtor = models.ForeignKey(RealtorUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.street + ", " + self.city + ", " + self.state + ", " + self.zip

