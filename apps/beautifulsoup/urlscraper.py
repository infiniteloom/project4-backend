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
    'https://www.compass.com/homes-for-sale/_map/mapview=41.69125189087717,-73.67678056005388,41.23070881554308,-73.99675736669451/price.min=425k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=41.31987607858595,-73.86880184751635,40.390254627043724,-74.5087554607976/price.min=425k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=42.75937320781332,-74.61276769085157,41.84936884760099,-75.25409459514843/price.min=425k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=40.94646206869337,-73.78396725910888,40.713963575871645,-73.94395566242919/price.min=425k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=40.739876697212324,-73.90153245345559,40.62336718364866,-73.98152665511574/price.min=425k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=41.95950103394698,-74.30267513287292,41.50087486692388,-74.62265193951355/price.min=425k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=42.13384557493043,-73.04956830745847,41.21582231944765,-73.68952192073972/price.min=425k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=41.410202223388396,-72.31369478478442,41.179340280337904,-72.47368318810473/price.min=900k/',
    'https://www.compass.com/homes-for-sale/_map/mapview=40.866261044035014,-73.86248188690134,40.63348106991663,-74.02247029022165/price.min=2m/',
    'https://www.compass.com/homes-for-sale/_map/mapview=41.60845759224359,-73.88417588277268,41.147324927495916,-74.2041526894133/price.min=2m/',
    'https://www.compass.com/homes-for-sale/_map/mapview=42.02310014075104,-74.4249357604212,41.56492994464449,-74.74491256706183/price.min=2m/'
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

