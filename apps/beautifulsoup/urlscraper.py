import bs4 as bs
import urllib.request
import csv
import re


"""
This function scrapes the thumbnails page of regional listings and gathers the urls of each individual listing
which will then be passed along to the main scraper.py to retrieve individual house listings and add them to a seed data file "house-listings.csv"
"""
# make a scraper that collects the urls of of all a tags with the that class
# grab href and create a list of all the urls
# run a loop through the list
# run this code per the list


