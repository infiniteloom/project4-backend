import bs4 as bs
import urllib.request
import csv
import re
from selenium import webdriver





img_page = urllib.request.urlopen('https://www.compass.com/listing/1084-highway-55a-napanoch-ny-12458/591790390221494241/').read()
image_soup = bs.BeautifulSoup(img_page, features="html.parser")
image_soup_b = image_soup.body
#print(image_soup_b)


info_page = urllib.request.urlopen('https://www.compass.com/listing/1084-highway-55a-napanoch-ny-12458/591790390221494241/').read()
info_soup = bs.BeautifulSoup(info_page, features="html.parser")
body = info_soup.body
table = info_soup.find('table', class_="data-table__TableStyled-ibnf7p-0 bhHpMT")
table_rows = table.find_all('tr')
info = body.find_all('div', class_="property-information__FieldSection-sc-1il5vdr-7")


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
    "image1": '',
    "image2": '',
    "image3": '',
    "image4": ''
}

# Get description
house['description'] = body.find('div', class_="sc-fzoWqW eoVQRn").text


# Get price
price_poss = body.find_all('div', class_="textIntent-title2")
price = []
for pr in price_poss:
    if '$' in pr.text:
        price.append(int(pr.text[1:].replace(",", "")))
house['price'] = price[0]


# Get address
house['street'] = body.find('p', class_="summary__StyledAddress-e4c4ok-6").text
address = body.find('div', class_="summary__StyledAddressCaption-e4c4ok-7").text
split = address.split()
house['city'] = split[0][:-1]
house['state'] = split[1]
house['zip'] = split[2]


# Get home_size, bed, bath
for inf in info:
    if 'Living Area: ' in inf.text:
        area = inf.text[(len('Living Area: ')):]
        house['home_size'] = float(inf.span.text)
    if 'Bedrooms Total:' in inf.text:
        house['bed'] = int(inf.span.text)
    if 'Bathrooms Full:' in inf.text:
        house['bath'] = int(inf.span.text)


# Get year_built, lot_size, type, county
for tr in table_rows:
    td = tr.find_all('td')
    for i in range (len(td)-1):
        if td[i].text == 'Year Built':
            house['year_built'] = int(td[i+1].text)
        if td[i].text == 'Lot Size':
            split = td[i + 1].text.split(" ", 1)
            house['lot_size'] = float(split[0])
        if td[i].text == "Compass Type":
            house['type'] = td[i+1].text
        if td[i].text == "County":
            house['county'] = td[i+1].text

print(house)




################ Add this house to the csv file "house-listings.csv" ################

file = csv.writer(open('house-listings.csv', 'w'))
file.writerow(["type", "city", "state", "zip", "street", "year_built", "bed", "bath", "home_size", "lot_size", "price", "description", "image1", "image2", "image3", "image4"])

# Add this house as a row to the csv.
file.addrow([house['type'], house['city'], house['state'], house['zip'], house['street'], house['year_built'], house['bed'], house['bath'], house['home_size'], house['lot_size'], house['price'], house['description'], house['image1'], house['image2'], house['image3'], house['image4']])

