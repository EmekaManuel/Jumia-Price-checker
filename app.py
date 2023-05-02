import requests ## directing our url
from bs4 import BeautifulSoup ## scraping the data from the web
import os
import smtplib ## for sending mails
from email.message import EmailMessage 

email_id = os.environ.get("")
email_pass= os.environ.get("")


URL = "https://www.jumia.com.ng/iphone-xs-max-64gb-gold-free-case-and-screen-guide-apple-mpg1719406.html"

headers = {
    'user-Agents': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

## getting the elements from the company webpage using the inspect element func
title = soup.find('h1', class_="-fs20 -pts -pbxs")
price = soup.find('span', class_="-b -ltr -tal -fs24").get_text()
## convert price to regular integers by elim commas
converted_price = int(price[2:].replace(",",""))
## check if data was fetched from the site
if title and price:
    print(title.get_text().strip())
    print(converted_price)

else:
    print('Product title not found')
    print('Product price not found')

## define a function to send me an email once the price goes lower then current price
if converted_price < 300000:
    send_mail()
    
def send_mail():
    msg = EmailMessage()
    msg['Subject'] = "Product price fall down"
    msg['From'] = email_id
    msg['To'] "marrnuel123@gmail.com"
    