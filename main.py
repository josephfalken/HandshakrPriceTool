from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    r = requests.get('https://google.com')
    soup = BeautifulSoup(r.text)
    navLinks = soup.find_all("a", class_ = "gb1")
    return str(navLinks)

#each route is an api call to my microservice --

@app.route('/getprices/<item>')
def getprices (item):
    ebayURL = f'https://www.ebay.com/sch/i.html?_nkw={item}&LH_Complete=1'
    r = requests.get(ebayURL)
    soup = BeautifulSoup(r.text)
    prices = soup.find_all("span", class_="s-item__price")
    return str (prices)