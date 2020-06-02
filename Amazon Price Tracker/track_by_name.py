import requests
from bs4 import BeautifulSoup
import os

def write_items(mode):
    search_query = input("Please type in the exact product name you want to track the prize of:\n")
    expected_price = input("What price are you expecting: ")
    with open('items.txt', mode) as f:
        f.write(f'{search_query}, {expected_price}\n')
    f.close()

def track_price(search_query, expected_price):
    search_query = search_query.replace(" ", "+")
    url = f'https://www.amazon.in/s?k={search_query}&ref=nb_sb_noss'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.content, "html.parser")

    title = soup.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
    price = soup.find('span', {'class': 'a-price-whole'}).text.replace(",", "")

    if int(price) <= int(expected_price):
        slug = soup.find('a', {'class': 'a-link-normal a-text-normal'})['href']
        link = 'https://www.amazon.in' + slug

        print(f'Congrats, currently price of {title} is Rs {int(price):,}')
        print(f'Check out the link below:\n{link}')
    else:
        print(f'Sorry currently the price is Rs {int(int(price) - int(expected_price)):,} higher than you expected.')
        print(f'The current price of {title} is Rs {int(price):,}')

def read_items():
    f = open('items.txt', 'r')
    items = f.readlines()
    for item in items:
        name = item.split(', ')[0]
        price = item.split(', ')[1]
        print(f'\nJust a sec, fetching the current price of {name.title()}')
        try:
            track_price(name, price)
        except:
            print('Either your requests limit exceeded or your internet connection is slow, Please try again after 24HRS.')

path = os.getcwd() + '\\items.txt'

if os.path.exists(path) and os.path.getsize(path) > 0:
    search_new = input("Do you want to track price of new product(Y/N): ")
    if search_new.upper() == 'Y':
        write_items('a') # appending new products
        read_items()
    else:
        read_items()
else:
    write_items('w') # writing initial product
    read_items()

print('\n**If these are not the product(s) you expected or you want to change expected price of some existing product, you can change the name and price in the text file named items.txt')
