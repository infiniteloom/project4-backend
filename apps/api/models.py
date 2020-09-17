from django.db import models
from apps.authentication.models import User



#### Listing Model
class Listing(models.Model):
    # Properties:
    type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()
    street = models.CharField(max_length=100)
    year_built = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    home_size = models.IntegerField() #square feet
    lot_size = models.FloatField()  # acres
    price = models.FloatField()
    description = models.TextField()
    # should i change these images into a one listing has many images and create a model for images?
    image1 = models.TextField(default=None)
    # image2 = models.TextField(default=None)
    # image3 = models.TextField(default=None)
    # image4 = models.TextField(default=None)
    # Relationships:
    interested_buyers = models.ManyToManyField(User, related_name='interested_buyers', blank=True)
    realtor = models.ForeignKey(User, on_delete=models.CASCADE) # realtor can have many listings 1:N
    # Time stamps:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.street + ", " + self.city + ", " + self.state + ", " + str(self.zip)

