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
| Day 1 | Create serializer for Realtor                                    | Incomplete |
| Day 1 | Create serializer for Buyer                                      | Incomplete |
| Day 1 | Create serializer for Listing                                    | Incomplete |
| Day 1 | Create model for Realtor                                         | Incomplete |
| Day 1 | Create model for Buyer                                           | Incomplete |
| Day 1 | Create model for Listing                                         | Incomplete |
| Day 1 | Create urls for Realtor                                          | Incomplete |
| Day 1 | Create urls for Buyer                                            | Incomplete |
| Day 1 | Create urls for Listing                                          | Incomplete |
| Day 1 | Create comma-separated seed data - import into Python            | Incomplete |
| Day 1 | Connect Buyer and Realtor to Auth                                | Incomplete |
| Day 2 | 'Create' view for listings                                       | Incomplete |
| Day 2 | 'Edit' view for listings                                         | Incomplete |
| Day 2 | 'Destroy' view for listings                                      | Incomplete |
| Day 2 | 'Index' and get by id views for listings                         | Incomplete |
| Day 2 | Testing of all end points                                        | Incomplete |




## Project Description


### Haven 
<i>Ha•ven /ˈhāvən/ (noun) a place of safety or refuge.</i>

Haven is a web application to showcase real estate listings. Haven is available for public browsing and offers additional features such as saving favorite homes and full CRUD functionality for realtors upon registration.

The front-end is built with HTML, CSS and JavaScript using Vue.js and Bootstrap. 
The backend is built with Python and PostgreSQL using Django. 


#### Realtor Model
Realtor Model Properties:
- region = dropdown menu 
- city = models.CharField(max_length=100)
- zip = models.IntField(max_length=10)
- name = models.CharField(max_length=100)
- company = models.CharField(max_length=100)
- listings = listings belong to Realtor, referenced relationship

#### Buyer Model
Buyer Model Properties:
- name = models.CharField(max_length=100)
- email = models.CharField(max_length=100)
- favorites = favorite a listing, listing belongs to Buyer?


#### Listing Model
Listing Model Properties:
- type = dropdown menu (house, land, condo, apartment)
- city = models.CharField(max_length=100)
- state = drop down menu, 2 letters
- zip = models.IntegerField(max_length=10)
- street = models.CharField(max_length=100)
- year_built = models.IntegerField(max_length=4)
- bed = drop down menu could be cool
- bath = drop down menu
- home_size = models.IntegerField(max_length=7) (sq feet)
- lot_size = models.IntegerField(max_length=7)   (sq feet)
- price =  models.IntegerField(max_length=10)   
- description = models.TextField()
- images = file drop!!!!!!!!!!!!!!!
- **created_at (if less than 14 days old, add a ‘new’ sticker)
- created_by = listings belong to Realtor



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
| Import seed data csv    |    H     |     3 hr       |       hrs     |      hrs    |
| Authorization app       |    H     |     2 hr       |       hrs     |      hrs    |
| Realtor and buyer models|    H    |     3 hrs      |       hrs     |      hrs    |
| Create full CRUD views for listings|  H  |     3 hrs      |       hrs     |      hrs    |
| Total                   |          |     11 hrs     |       hrs     |      hrs    |

#### PostMVP

| Component                                      | Priority | Estimated Time | Time Invested | Actual Time |
| ---------------------------------------------- | :------: | :------------: | :------------: | :---------: |
| Sorting routes for listings                    |    H     |     2 hrs      |      hrs      |      hrs   |
| Configure Geopy, connect with Open Street Maps |    M     |     4 hrs      |      hr       |     hr     |
| Total                                          |          |     6 hrs   |      hrs      |    hrs     |

## Additional Libraries

- Geopy (create coordinates from listing's street addresses and connect with Open Street Map )

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description


## Issues and Resolutions

Use this section to list of all major issues encountered and their resolution.

**ERROR**: 
**RESOLUTION**:
