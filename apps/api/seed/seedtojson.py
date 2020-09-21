

import csv
import json


with open('listings.csv', 'r') as csv_file:

    csvreader = csv.reader(csv_file)

    # Skips header line in csv_file.
    next(csvreader)
    listings = []
    counter = 1

    for row in csvreader:
        print(row[13])
        # Creates references to realtor based on what county the listing is in.
        if row[13] == 'Ulster County':
            realtor = 1

        elif row[13] == 'Greene County':
            realtor = 2

        elif row[13] == 'Delaware County':
            realtor = 3

        elif row[13] == 'Dutchess County':
            realtor = 4

        elif row[13] == 'Fairfield County':
            realtor = 5

        elif row[13] == 'Herkimer County':
            realtor = 6

        elif row[13] == 'Sullivan County':
            realtor = 7

        elif row[13] == 'Oneida County':
            realtor = 8

        elif row[13] == 'Westchester County':
            realtor = 9

        elif row[13] == 'Putnam County':
            realtor = 10

        elif row[13] == 'Litchfield County':
            realtor = 11

        # In case any extra counties are unaccounted for (base case)
        else:
            realtor = 11


        listing={
            "model": "api.listing",
            "pk": counter,
            "fields": {
                "type":row[0],
                "city":row[1],
                "county":row[13],
                "state":row[2],
                "zip":row[3],
                "street":row[4],
                "year_built":row[5],
                "bed":row[6],
                "bath":row[7],
                "home_size":row[8],
                "lot_size":row[9],
                "price":row[10],
                "description":row[11],
                "image1":row[12],
                "realtor":realtor,
                "created_at":'2020-09-16T19:24:17+0000',
                "updated_at":"2020-09-16T19:24:17+0000"
            }
        }
        counter += 1
        listings.append(listing)

    with open('seed.json', 'w') as jsonfile:
        json.dump(listings, jsonfile)
        jsonfile.write('\n')


