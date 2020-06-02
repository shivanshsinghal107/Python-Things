# Python-Things
## Projects and Automations built with Python
I built these projects for fun, intended to ***Automate the Boring Stuff with Python***, exploring python to build some cool things.

### A Python app to Track Amazon Prices
I built a Python app to track amazon price(s) of my desired product(s), there are two apps:
1) **Track price by URL** - Track price of any product by replacing the url of that amazon product, expected price & your email in the Python script (pretty accurate, and you will be notified on your email when price will become lower than your expected price)<br>
Technologies used: ***Web Scraping(requests, BeautifulSoup), smtplib(for sending email)***
2) **Track price by product name** - Track prices of multiple products by just telling the product name, and expected price (accurate if you give the product name exact, you'll be getting the product link to buy if the price feel down)<br>
Technologies used: ***Web Scraping(requests, BeautifulSoup)***

I learnt basics of Web Scraping and automatic email sending using `smtplib` of Python by building this project.

### YouTube Downloader (A Python tkinter GUI app)
Give the URL of the YouTube video, it will fetches all available resolutions of that video with their sizes in MBs, and lists out the options to download on the Command Prompt.<br>
It also keeps track of the progress of download by showing percentage downloaded on the cmd window.<br>
Technologies used: ***tkinter, pytube***

I learnt basics of tkinter(building python a GUI app) and `pytube` to interact with YouTube with help of python.

<img src="YouTube Downloader/youtube downloader.PNG" width="425"/>
