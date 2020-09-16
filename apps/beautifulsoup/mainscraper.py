import bs4 as bs
import urllib.request
import csv

# import re
# from selenium import webdriver


"""
This file opens each individual house's URL on the imported list of URLs from urlscraper.py (a file that 
scrapes href tags from the thumbnails as well as img srcs of the thumbnails of homes on Compass's regional listings page)
Each row in the final resulting 'house-listings.csv' file is representative of all descriptive information scraped from 
each individual home. 

"""

with open('listings-urls.csv', 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    # Skips header line in csv_file.
    next(csvreader)

    file = csv.writer(open('house-listings.csv', 'w'))
    file.writerow(
        ["type", "city", "state", "zip", "street", "year_built", "bed", "bath", "home_size", "lot_size", "price",
         "description", "image1"])




    # Loop through this entire scraping function per row (contains single listing URL) in csv_file
    for row in csvreader:
        print(row[0])
        info_page = urllib.request.urlopen(row[0]).read()

        #for testing single page:
        # info_page = urllib.request.urlopen('https://www.compass.com/listing/12-18-ballard-road-mongaup-valley-ny-12762/594433160153028873/').read()

        info_soup = bs.BeautifulSoup(info_page, features="html.parser")
        body = info_soup.body

        # This is the dictionary that holds all of the gathered information and will be appended to the csv.
        house = {
            "type": '',
            "city": '',
            "state": '',
            "zip": 0,
            "street": '',
            "year_built": 0,
            "bed": 0,
            "bath": 0,
            "home_size": 0,
            "lot_size": 0,
            "price": 0,
            "description": '',
            "image1": ''
        }

        # Used to check if any numbers are in a string, conditional
        nums = ["0","1","2","3","4","5","6","7","8","9"]


        # Get description
        if body.find('div', class_="sc-fzoWqW eoVQRn"):
            house['description'] = body.find('div', class_="sc-fzoWqW eoVQRn").text




        # Get address (street, city, state, zip)
        address = body.select('div[class*="summary__StyledAddressCaption"]')
        address_text = address[0].text
        addr_split = address_text.split(",")
        house['city'] = addr_split[0].strip(' ')
        house['state'] = (addr_split[1].lstrip(' ').split(' '))[0]
        house['zip'] = int((addr_split[1].lstrip(' ').split(' '))[1])


        # Get price, bed, bath
        info = body.select('div[class*="summary__Content"]')



        for inf in info:
            # print(inf.text)
            if 'Price' in inf.text:
                house['price'] = float(inf.text.replace(',', '').strip('$').replace('Price', ''))
            if 'Beds' in inf.text:
                for num in nums:
                    if num in inf.text:
                        print(inf.text)
                        house['bed'] = int(inf.text.replace('Beds', ''))
            if 'Baths' in inf.text:
                for num in nums:
                    if num in inf.text:
                        if house['bath'] == 0:
                            house['bath'] = int(inf.text.replace('Baths', ''))
            if house['city'] in inf.text:
                ind = inf.text.index(house['city'])
                house['street'] = inf.text[:ind]
            if 'Sq.' in inf.text and '$' not in inf.text:
                ind = inf.text.index('Sq.')
                size = inf.text[:ind].replace(',', '').replace(' ', '')
                if ( ''.join(filter(str.isdigit, size) ) ):
                    house['home_size']= int(size)






        # Get year_built, lot_size, type, county

        table = info_soup.find('table', class_="data-table__TableStyled-ibnf7p-0 bhHpMT")
        table_rows = table.find_all('tr')

        for tr in table_rows:
            td = tr.find_all('td')
            for i in range(len(td)-1):
                if td[i].text == 'Year Built':
                    for num in nums:
                        if num not in td[i+1].text:
                            house['year_built'] = 0
                        else:
                            house['year_built'] = int(td[i+1].text)
                if td[i].text == 'Lot Size':
                    if 'AC' in td[i+1].text:
                        ind = td[i+1].text.index('AC')
                        size = td[i+1].text[:ind].replace(' ', '').replace(',', '')
                        house['lot_size'] = float(size)
                if td[i].text == "Compass Type":
                    house['type'] = td[i+1].text
                if td[i].text == "County":
                    house['county'] = td[i+1].text



        # Get one image per listing:
        # print(body.find('img').get('src'))
        house['image1'] = 'https://' + (body.find('img').get('src'))



        ################ Add this house to the csv file "house-listings.csv" ################

        print(house)

        # Add this house as a row to the csv.
        file.writerow([house['type'], house['city'], house['state'], house['zip'], house['street'], house['year_built'], house['bed'], house['bath'], house['home_size'], house['lot_size'], house['price'], house['description'], house['image1']])
