# A Python App that Tracks Amazon Prices

Idea Credit: https://www.youtube.com/watch?v=Bg9r_yLk7VY&list=WL&index=21&t=0s

I've always wondered wouldn't it be great if I always get notified or get to track the price of product that I wanted to buy for so long when the price goes down to something I would prefer it buying.<br>
And guess what, that's what got me to build something with Python to do it for me.
So I built a Python app to track price(s) of my desired product(s), there are two apps:
1) **Track price by URL** - Track price of any product by replacing the url of that amazon product, expected price & your email in the Python script (pretty accurate, and you will be notified on your email when price will become lower than your expected price)<br>
Technologies used: ***Web Scraping(requests, BeautifulSoup), smtplib(for sending email)***
2) **Track price by product name** - Track prices of multiple products by just telling the product name, and expected price (accurate if you give the product name exact, you'll be getting the product link to buy if the price feel down)<br>
Technologies used: ***Web Scraping(requests, BeautifulSoup)***

Just one thing is there which is not good about this app, it is that you'll have to run the python script everytime, if you want to get notified, it do not keep running automatically all time.

I just built this thing for fun, intended to ***Automate the Boring Stuff with Python***.<br>
I learnt basics of Web Scraping and automatic email sending using `smtplib` of Python by building this project.
