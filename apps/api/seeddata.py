import csv
import django
from api.models import Listing
from apps.authentication.models import User





"""
THIS SECTION CREATES NEW INSTANCES OF USERS AS REALTORS 
EACH LISTING WILL BE ASSIGNED TO A REALTOR BASED ON COUNTY
"""
# Create realtors for seed data:
realtor1 = User(
    id=1,
    email="mika@mika.com",
    username='mikamika',
    password='buybuy123123',
    first_name='Mika',
    last_name='Akim',
    county='Ulster County',
    city="Kingston",
    zip="12401",
    company="Ulster County Realtors, Co.",
    user_type='realtor'
)

realtor2 = User(
    id=2,
    email="john@john.com",
    username='johnjohn',
    password='buybuy123123',
    first_name='John',
    last_name='Mistermister',
    county='Greene County',
    city="Catskill",
    zip="12414",
    company="Catskill Homes, Co.",
    user_type='realtor'
)

realtor3 = User(
    id=3,
    email="hannah@hannah.com",
    username='hannahhannah',
    password='buybuy123123',
    first_name='Hannah',
    last_name='Lewis',
    county='Delaware County',
    city="Delhi",
    zip="13753",
    company="Delhi's Finest",
    user_type='realtor'
)

realtor4 = User(
    id=4,
    email="nico@nico.com",
    username='niconico',
    password='buybuy123123',
    first_name='Nico',
    last_name='Matsuda',
    county='Dutchess County',
    city="Poughkeepsie",
    zip="12601",
    company="Dutchess County Realtors, Co.",
    user_type='realtor'
)

realtor5 = User(
    id=5,
    email="liza@liza.com",
    username='lizaliza',
    password='buybuy123123',
    first_name='liza',
    last_name='johnson',
    county='Fairfield County',
    city='Fairfield',
    zip="06824",
    company="Fairfield County Realtors, Co.",
    user_type='realtor'
)

realtor6 = User(
    id=6,
    email="summer@summer.com",
    username='summersummer',
    password='buybuy123123',
    first_name='Summer',
    last_name='Akana',
    county='Herkimer County',
    city="Herkimer",
    zip="13350",
    company="Herkimer County Realtors, Co.",
    user_type='realtor'
)

realtor7 = User(
    id=7,
    email="brendan@brendan.com",
    username='brendanbrendan',
    password='buybuy123123',
    first_name='Brendan',
    last_name='Muhly',
    county='Sullivan County',
    city="Monticello",
    zip="12701",
    company="Sullivan County Realtors, Co.",
    user_type='realtor'
)

realtor8 = User(
    id=8,
    email="jeremy@jeremy.com",
    username='jeremyjeremy',
    password='buybuy123123',
    first_name='Jeremy',
    last_name='Mendo',
    county='Oneida County',
    city="Oneida",
    zip="13032",
    company="Oneida County Realtors, Co.",
    user_type='realtor'
)

realtor9 = User(
    id=9,
    email="gina@gina.com",
    username='ginagina',
    password='buybuy123123',
    first_name='Gina',
    last_name='Kristin',
    county='Westchester County',
    city="Westchester",
    zip="10504",
    company="Westchester County Realtors, Co.",
    user_type='realtor'
)

realtor10 = User(
    id=10,
    email="sara@sara.com",
    username='sarasara',
    password='buybuy123123',
    first_name='Sara',
    last_name='Gold',
    county='Putnam County',
    city="Patterson",
    zip="12563",
    company="Putnam County Realtors, Co.",
    user_type='realtor'
)


realtor11 = User(
    id=11,
    email="michael@michael.com",
    username='michaelmichael',
    password='buybuy123123',
    first_name='Michael',
    last_name='Thayer',
    county='Litchfield County',
    city="Litchfield",
    zip="06750",
    company="Litchfield County Realtors, Co.",
    user_type='realtor'
)

# save all new realtor instances of User model
realtor1.save()
realtor2.save()
realtor3.save()
realtor4.save()
realtor5.save()
realtor6.save()
realtor7.save()
realtor8.save()
realtor9.save()
realtor10.save()
realtor11.save()









"""
THIS SECTION IMPORTS THE HOUSE LISTINGS SCRAPED FROM COMPASS.COM AND SAVED INTO A "house-listings.csv" USING BEAUTIFULSOUP
"""

with open('house-listings.csv', 'r') as csv_file:
    csvreader = csv.reader(csv_file)

    # Skips header line in csv_file.
    next(csvreader)

    # Loops through each row in the csv
    for row in csvreader:

        # Creates references to realtor based on what county the listing is in.
        if row[12] == 'Ulster County':
            realtor = realtor1

        if row[12] == 'Greene County':
            realtor = realtor2

        if row[12] == 'Delaware County':
            realtor = realtor3

        if row[12] == 'Dutchess County':
            realtor = realtor4

        if row[12] == 'Fairfield County':
            realtor = realtor5

        if row[12] == 'Herkimer County':
            realtor = realtor6

        if row[12] == 'Sullivan County':
            realtor = realtor7

        if row[12] == 'Oneida County':
            realtor = realtor8

        if row[12] == 'Westchester County':
            realtor = realtor9

        if row[12] == 'Putnam County':
            realtor = realtor10

        if row[12] == 'Litchfield County':
            realtor = realtor11

        # In case any extra counties are unaccounted for (base case)
        else:
            realtor = realtor11



        # Create a new instance of Listing object
        new_listing = Listing(
            type=row[0],
            city=row[1],
            county=row[12],
            state=row[2],
            zip=row[3],
            street=row[4],
            year_built=row[5],
            bed=row[6],
            bath=row[7],
            home_size=row[8],
            lot_size=row[9],
            description=row[10],
            image1=row[11],
            interested_buyers=[],
            realtor=realtor
        )

        new_listing.save()




"""
THIS SECTION CREATES NEW USERS AS BUYERS TO SAVE AND FAVORITE HOME LISTINGS
"""


buyer1 = User(
    id=12,
    email="angel@angel.com",
    username='angelangel',
    password='buybuy123123',
    user_type='buyer'
)

buyer2 = User(
    id=12,
    email="taylor@taylor.com",
    username='taylortaylor',
    password='buybuy123123',
    user_type='buyer'
)

buyer3 = User(
    id=12,
    email="misty@misty.com",
    username='mistymisty',
    password='buybuy123123',
    user_type='buyer'
)

# Save new instances of User model as buyers
buyer1.save()
buyer2.save()
buyer3.save()