from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# allows us to access the JWT settings
from rest_framework_jwt.settings import api_settings

# sets up the JWT payload (data sent with token)
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

"""
Default Django Authorization User Model Documentation:
https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_staff
"""
# Create your models here.


# allows us to create a regular user or a superuser
class UserManager(BaseUserManager):

    def create_user(self, email, username, password, first_name=None, last_name=None, user_type='buyer'):

        if username is None:
            raise TypeError("Users must have a username.")
        if email is None:
            raise TypeError("Users must have an email address.")


        # create the user object
        # self.normalize_email is inbuilt method to django that strips white space and lowercases
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            # county=county,
            # city=city,
            # zip=zip,
            # company=company,
            user_type=user_type
        )

        user.set_password(password)
        user.save()
        return user



    # this is creating a superuser administrator
    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Superusers must have a password.")
        user = self.create_user(username, email, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user



# This class is for people who are using the site, logging in etc. Not for superusers
class User(AbstractBaseUser, PermissionsMixin):

    # db_index gives the user a unique index in the database
    # unique ensures the username doesn't already exist in database
    # these are all built in methods to the AbstractBaseUser
    email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    county = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=100, null=True)
    user_type = models.CharField(max_length=255, default='realtor')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] # this is an array, could have more required fields

    # tells Django that the first UserManager class will manage objects of this type
    objects = UserManager()



    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()
    """
    Generates a JSON Web Token that stores this(self) object /user instance 
    and has an expiration date set to 60 days from creation of token
    """

    # a single underscore before a method name is a 'PROTECTED' method.

    def _generate_jwt_token(self):
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        return token
