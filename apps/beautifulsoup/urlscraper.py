import bs4 as bs
import urllib.request
import csv


"""
This function scrapes the thumbnails page of regional listings and gathers the urls of each individual listing
which will then be passed along to the main scraper.py to retrieve individual house listings and add them to a seed data file "house-listings.csv"
"""

# Create a csv file to write to, add the header
file = csv.writer(open('listings-urls.csv', 'w'))
file.writerow(['url'])

# Gather primary information from body of multiple regional listings page.

regional_listings_pages = [
    'https://www.compass.com/homes-for-sale/_map/price.min=500k/property-type=Single%20Family,Multi%20Family,Land/status=active/mapview=42.11672554820275,-74.31565783148434,41.642296386124734,-74.8457481635156/',
    'https://www.compass.com/homes-for-sale/_map/price.min=500k/property-type=Single%20Family,Multi%20Family,Land/status=active/mapview=42.469542492018576,-74.14511221357468,41.99877214605945,-74.42595022626999/',
    'https://www.compass.com/homes-for-sale/_map/price.min=500k/property-type=Single%20Family,Multi%20Family,Land/status=active/mapview=43.141584051611744,-72.93039352691973,41.25768335673707,-74.05374557770098/',
    'https://www.compass.com/homes-for-sale/_map/price.min=500k/property-type=Single%20Family,Multi%20Family,Land/status=active/mapview=43.92411485141011,-74.32565719879473,42.064082490801866,-75.44900924957598/'
]
for page in regional_listings_pages:
    info_page = urllib.request.urlopen(page).read()
    info_soup = bs.BeautifulSoup(info_page, features="html.parser")
    body = info_soup.body


    # Gather all the URL links for individual house listings
    # Must add 'https://compass.com to the beginning of all gathered URLs
    for link in body.find_all('a', class_="uc-listingPhotoCard uc-listingCard uc-listingCard-has-photo"):
        ext = link.get('href')
        fullurl = ('https://www.compass.com' + ext)
        file.writerow([fullurl])

