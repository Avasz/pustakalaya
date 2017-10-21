#!/usr/bin/env python3

"""
Scrape some goodreads books
title
abstract
thumbnail
"""
import requests
from lxml import html
import string
import os
import random
import json


try:
    from django.conf import settings
except ImportError:
    pass


URL = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
page=1
ENDPAGE = 500
books = "/home/{0}/books.json".format(os.getlogin())



def saveimage(url):
    """
    method to save an image to disk
    """

    # Create a random image name
    image_name = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(6))
    # Add extension to image name
    image_name = "{0}.jpg".format(image_name)
    # Request an image from web
    print("image url", url)
    raw_image = requests.get(url)
    # Save image to disk or django Media root
    if raw_image.status_code != 200:
        print("Can't save image")
        return None

    # Location to write image
    try:
        MEDIA_ROOT = os.path.join(settings.MEDIA_ROOT, "uploads/goodreads")
    except NameError:
         MEDIA_ROOT = os.path.join(os.getcwd(), "images")

    image_name = os.path.join(MEDIA_ROOT, image_name)
    print(image_name)

    # If directory not exist create dir
    os.makedirs(os.path.dirname(image_name), exist_ok=True)

    with open(image_name, "wb") as thumbnail:
        for block in raw_image.iter_content(1024):
            if not block:
                break

            thumbnail.write(block)

    return os.path.join(image_name)



def scrape():
    for i in range(1, ENDPAGE+1):
        # Construct a url for each page
        url = "{0}?page={1}".format(URL, i)
        print("Scarping Page {}".format(i))

        # Request a page
        page =  requests.get(url)

        # If request not succed continue to next page
        if page.status_code != 200:
            print("Unknown Error in page {} while requesting ".format(i))
            continue

        # If success start scraping
        # It has 100 books per page

        # Create a tree
        tree = html.fromstring(page.content)

        for i in range(1, 101):
            title = "".join(tree.xpath('//*[@id="all_votes"]/table/tr['+ str(i) + ']/td[3]/a/span/text()'))
            image = "".join(tree.xpath('//*[@id="all_votes"]/table/tr['+str(i)+']/td[2]/div[2]/a/img/@src'))
            # Image location in disk
            image = saveimage(url)
            # Create json file
            with open(books, "a+") as json_file:
                book = dict(title=title, image=image)
                print("Writing data to file")
                json_file.write(json.dumps(book))


            print(title, image)



if __name__ == '__main__':
    scrape()
