
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs

url='https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq'

webpage = requests.get(url)
webcontent = webpage.content
htmlcontent = bs(webcontent, 'html.parser' )

for div in htmlcontent.findAll('div', attrs:={'class':'_3pLy-c row'}):
    name=div.find('div', attrs={'class':'_4rR01T'})
    rating=div.find('div', attrs={'class':'_3LWZlK'})

    
    print(name.text)
    print(rating.text)
