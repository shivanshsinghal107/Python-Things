import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/realme-RMA108-Realme-Buds-Wireless/dp/B07XJWTYM2/ref=sr_1_1?dchild=1&keywords=realme+wireless+earphones&qid=1589532606&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def check_price():
    page = requests.get(url, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()

    title = title.strip()
    price = price[2:].split(',')
    price = float("".join(price))

    if(price <= 1600):
        print("The current price of " + title + " is Rs " + str(price))
        send_mail()
    else:
        print("Sorry the price didn't fell down.")
        print("The current price of " + title + " is Rs " + str(price))

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # EHLO means ESMTP - Extended Simple Mail Transfer Protocol
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your email', 'password') # see the video tutorial from README.md file

    subject = 'Hurry up! Price fell down.'
    body = 'Check the amazon link\n'+url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email of sender',
        'email of reciever',
        msg
    )

    print("HEY, EMAIL HAS BEEN SENT!")

    server.quit()

check_price()
