# ebay.py
# ebayscraper module
# EBay scraper functionality

from bs4 import BeautifulSoup


def make_ebay_url(item):
    if item is None:
        return None
    if not item:
        return None
    # Use an f-string (formatted string literal) to
    # insert the item into the EBay URL
    return f'https://www.ebay.com/sch/i.html?_nkw={item}&LH_Complete=1'


def parse_ebay_page_and_extract_prices(html_source):
    soup = BeautifulSoup(html_source, features="html.parser")
    price_spans = soup.find_all("span", class_="s-item__price")
    prices = []
    i = 0
    for span in price_spans:
        if i > 1: # The first two prices on each scraped page appear invalid. Skip them
            # First we strip the currency symbol ($)
            price_string = span.text.strip('$')
            try:
                # Now try converting what's left to a floating point number
                price_number = float(price_string)
                prices.append(price_number)
            except ValueError:
                pass  # Ignore errors (skip over these)
        i += 1
    return prices


