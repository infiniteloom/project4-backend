# Project Overview

## Project

Link to completed project [here](https://haven-homes.netlify.app/)

Link to heroku [here](https://lt-project4-backend.herokuapp.com/)

Link to project frontend on GitHub [here](https://github.com/infiniteloom/project4-frontend)

Link to project backend on GitHub [here](https://github.com/infiniteloom/project4-backend)

## Project Schedule

| Day   | Deliverable                                                      | Status     |
| ----- | ---------------------------------------------------------------- | ---------- |
| Day 1 | Project description                                              | Completed  |
| Day 1 | Wireframes / Priority Matrix / Timeline `backend` and `frontend` | Completed  |
| Day 1 | Authorization                                                    | Completed  |
| Day 1 | Create serializer for User (Buyer and Realtor Types)             | Completed  |
| Day 1 | Create serializer for Listing                                    | Completed  |
| Day 1 | Create model for Listing                                         | Completed  |
| Day 1 | Create urls for Listing                                          | Completed  |
| Day 1 | Test Realtor User to Listings                                    | Completed  |
| Day 1 | Connect Buyer and Realtor to Auth                                | Completed  |
| Day 1 | 'Create' view for listings                                       | Completed  |
| Day 1 | 'Edit' view for listings                                         | Completed  |
| Day 1 | 'Destroy' view for listings                                      | Completed  |
| Day 1 | 'Index' and get by id views for listings                         | Completed  |
|       |                                                                  |            |
| Day 2 | Create urls for User (Buyer and Realtor Types)                   | Completed  |
| Day 2 | Create model for User (Buyer and Realtor Types)                  | Completed  |
| Day 2 | 'Realtor Listings' view for list view of realtor's listings      | Completed  |
| Day 2 | 'Favorites Listings' view for list view of buyer's favorite homes| Completed  |
| Day 2 | Adjust permissions for listings (index=public, create/update/destroy=realtor only)| Completed  |
|       |                                                                  |            |
| Day 2/3 | Use Beautiful Soup to scrape data, create csv for seed data set| Completed  |
| Day 3 | Create seed data template                                        | Completed  |
| Day 3 | Import seed data into database                                   | Completed |
|       |                                                                  |            |
| Day 3 |  Final testing of all end points                                 | Completed |




## Project Description


### Haven 
<i>Ha•ven /ˈhāvən/ (noun) a place of safety or refuge.</i>

Haven is a web application to showcase real estate listings. Haven is available for public browsing and offers additional features such as saving favorite homes and full CRUD functionality for realtors upon registration.

The front-end is built with HTML, CSS and JavaScript using Vue.js and Bootstrap. 
The backend is built with Python and PostgreSQL using Django. 


#### User Model
    class User(AbstractBaseUser, PermissionsMixin):
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
        zip = models.IntegerField(null=True)
        company = models.CharField(max_length=100, null=True)
        user_type = models.CharField(max_length=255, default='buyer')

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
        price = models.IntegerField()
        description = models.TextField()
        # should i change these images into a one listing has many images and create a model for images?
        image1 = models.TextField(default=None)
        image2 = models.TextField(default=None)
        image3 = models.TextField(default=None)
        image4 = models.TextField(default=None)
        # Relationships:
        interested_buyers = models.ManyToManyField(User, related_name='interested_buyers', blank=True)
        realtor = models.ForeignKey(User, on_delete=models.CASCADE) # realtor can have many listings 1:N
        # Time stamps:
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now_add=True)




## Wireframes
#### Mobile:

- [Home Page](https://res.cloudinary.com/infiniteloom/image/upload/v1599963622/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Landing_kd4h3z.png)
- [Home Page - Menu Expanded](https://res.cloudinary.com/infiniteloom/image/upload/v1599963622/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Landing_Menu_Expanded_dt8jr2.png)
- [Buyer Login](https://res.cloudinary.com/infiniteloom/image/upload/v1599963621/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Buyer_Login_cv7rcc.png)
- [Buyer Register](https://res.cloudinary.com/infiniteloom/image/upload/v1599963621/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Buyer_Register_gganag.png)
- [Realtor Login](https://res.cloudinary.com/infiniteloom/image/upload/v1599963621/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Realtor_Login_e5u9bm.png)
- [Realtor Register](https://res.cloudinary.com/infiniteloom/image/upload/v1599963622/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Realtor_Register_byhrxo.png)
- [Listings - List View](https://res.cloudinary.com/infiniteloom/image/upload/v1599963622/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Listings_ed90y4.png)
- [Realtor Admin Panel](https://res.cloudinary.com/infiniteloom/image/upload/v1600034789/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Admin_List_jnwlt0.png)
- [Create Listings Modal](https://res.cloudinary.com/infiniteloom/image/upload/v1600033539/Unit%2004%20-%20Project%20-%20Haven/Mobile/Mobile_Create_Listings_View_vadrhx.png)


#### Web:
- [Home Page](https://res.cloudinary.com/infiniteloom/image/upload/v1599963504/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Landing_uqntdt.png)
- [Home Page - User Menu Expanded](https://res.cloudinary.com/infiniteloom/image/upload/v1599965100/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Listings_User_Menu_Expanded_mp8vtz.png)
- [Buyer Login](https://res.cloudinary.com/infiniteloom/image/upload/v1599963503/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Buyer_Login_tclvje.png)
- [Buyer Register](https://res.cloudinary.com/infiniteloom/image/upload/v1599963504/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Buyer_Register_rh0l2c.png)
- [Realtor Login](https://res.cloudinary.com/infiniteloom/image/upload/v1599963503/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Realtor_Login_d1pqyb.png)
- [Realtor Register](https://res.cloudinary.com/infiniteloom/image/upload/v1599963502/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Realtor_Register_mwyvvw.png)
- [Listings - List View](https://res.cloudinary.com/infiniteloom/image/upload/v1599966783/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Listings_List_ejrkp2.png)
- [Listings - Map View](https://res.cloudinary.com/infiniteloom/image/upload/v1599966391/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Listings_Map_View_User_Menu_Expanded_oszn5d.png)
- [Realtor Admin Panel](https://res.cloudinary.com/infiniteloom/image/upload/v1600034781/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Admin_List_pvqb7k.png)
- [Create Listings Modal](https://res.cloudinary.com/infiniteloom/image/upload/v1600033562/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Create_Listings_View_ffzbfd.png)

#### Tablet:
- [Home Page](https://res.cloudinary.com/infiniteloom/image/upload/v1599963504/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Landing_uqntdt.png)
- [Buyer Login](https://res.cloudinary.com/infiniteloom/image/upload/v1599963503/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Buyer_Login_tclvje.png)
- [Buyer Register](https://res.cloudinary.com/infiniteloom/image/upload/v1599963504/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Buyer_Register_rh0l2c.png)
- [Realtor Login](https://res.cloudinary.com/infiniteloom/image/upload/v1599963503/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Realtor_Login_d1pqyb.png)
- [Realtor Register](https://res.cloudinary.com/infiniteloom/image/upload/v1599963502/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Realtor_Register_mwyvvw.png)
- [Listings - List View](https://res.cloudinary.com/infiniteloom/image/upload/v1599966783/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Listings_List_ejrkp2.png)
- [Realtor Admin Panel](https://res.cloudinary.com/infiniteloom/image/upload/v1600034781/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Admin_List_pvqb7k.png)
- [Create Listings Modal](https://res.cloudinary.com/infiniteloom/image/upload/v1600033562/Unit%2004%20-%20Project%20-%20Haven/Web/Web_Create_Listings_View_ffzbfd.png)




## Time/Priority Matrix

[A graph of all features]() based on their priority and the time estimated to complete each.

### MVP/PostMVP

The backend functionality of Haven.com is divided into two separate lists: MPV and PostMVP. 

#### MVP:
-	Create authorization app
-	Create realtor and buyer models 
-   Create full CRUD controllers/views for listings


#### POST-MVP:
-  Sorting routes for listings
-  Configure Geopy to create coordinates from listing's street addresses and connect with Open Street Map 

<br/>

## Functional Components

#### MVP

| Component                     | Priority | Estimated Time | Time Invested | Actual Time |
| ----------------------------- | :------: | :------------: | :------------:| :---------: |
| Scrape data for seed    |    H     |     4 hr       |       6hrs     |      6hrs    |
| Import seed data csv    |    H     |     2 hr       |       2hrs     |      2hrs    |
| Authorization app       |    H     |     2 hr       |       2hrs     |      2hrs    |
| Realtor and buyer models|    H     |     3 hrs      |       2hrs     |      2hrs    |
| Create full CRUD views for listings|  H  |     3 hrs      |       4hrs     |      4hrs    |
| Total                   |          |     11 hrs     |       16hrs     |      16hrs    |

#### PostMVP

| Component                                      | Priority | Estimated Time | Time Invested | Actual Time |
| ---------------------------------------------- | :------: | :------------: | :------------: | :---------: |
| Sorting routes for listings                    |    H     |     2 hrs      |      hrs      |      hrs   |
| Configure Geopy, connect with Open Street Maps |    M     |     4 hrs      |      hr       |     hr     |
| Total                                          |          |     6 hrs   |      hrs      |    hrs     |

## Additional Libraries

- Beautiful Soup (web scraper)
- Geopy (create coordinates from listing's street addresses and connect with Open Street Map )
- Django REST Framework (to build REST API)
- Django REST Framework JWT (create tokens for authorization)


