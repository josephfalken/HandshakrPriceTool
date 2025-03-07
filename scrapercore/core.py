# core.py
# scrapercore module
# Core scraper functionality

from datetime import datetime

import requests
from ebayscraper import ebay
from scrapercache import cache


def get_price(item):

    #First lookup in the cache
    cached_response = cache.lookup(item)
    if not cached_response is None:
        return cached_response

    #Map the item name into an EBay URL
    ebay_url = ebay.make_ebay_url(item)
    if ebay_url is None:
        return None

    #Make the http request to the 3rd party server
    response = requests.get(ebay_url)
    #If we got an error back or no response at all, exit
    if response is None:
        return None
    if response.status_code != 200:
        return None
    ebay_scraper_prices = ebay.parse_ebay_page_and_extract_prices(response.text)
    if ebay_scraper_prices is None:
        return None

    #Cache the result for next time
    cache.add_to_cache(item, ebay_scraper_prices)

    #And return the response to we can send it back to the caller
    return ebay_scraper_prices


def list_cache():
    return cache.enumerate_cache()
