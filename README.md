# Python-Things
## Projects and Automations built with Python
I built these projects for fun, intended to ***Automate the Boring Stuff with Python***, exploring python to build some cool things.

### A Python app to Track Amazon Prices
I built a Python app to track amazon price(s) of my desired product(s), there are two apps:
1) **Track price by URL** - Track price of any product by replacing the url of that amazon product, expected price & your email in the Python script (pretty accurate, and you will be notified on your email when price will become lower than your expected price)<br>
Technologies used: ***Web Scraping(requests, BeautifulSoup), smtplib(for sending email)***
2) **Track price by product name** - Track prices of multiple products by just telling the product name, and expected price (accurate if you give the product name exact, you'll be getting the product link to buy if the price feel down)<br>
Technologies used: ***Web Scraping(requests, BeautifulSoup)***

I learnt basics of Web Scraping and automatic email sending using `smtplib` library of Python by building this project.

### YouTube Downloader (A Python GUI app)
I built a python GUI app to download YouTube videos on my local computer, which is basically a **YouTube Downloader**.
Firstly, I built YTD with `tkinter`, then I learned `PyQt5` & qt designer and built another YTD having a nice looking GUI, and which finally concluded my project and learnings.

### `PyQt5` YTD
- Type/Paste in the URL of YouTube video
- Click on Proceed and it will show all resolutions options of the video as list with their sizes in MBs, it also shows the thumbnail of the YouTube video on the right space by fetching from YouTube.
- Choose the video you want to download and location at which it is to be saved.
- Click on the Download button and you'll see the downloaded percent on the progress bar.
- Technologies used: ***PyQt5, pytube, urllib***

<img src="YouTube Downloader/ytd_pyqt.PNG">

### `tkinter` YTD
- Give the URL of YouTube video, and it will fetch all available resolutions of that video with their sizes in MBs, and lists out the options to download on the Command Prompt.
- It also keeps track of the progress of download by showing percentage downloaded on the cmd window.
- Technologies used: ***tkinter, pytube***

<img src="YouTube Downloader/youtube downloader.PNG" width="500" height="400">

Through this project I learnt basics of `tkinter` & got to learn more than basics of `PyQt5`, also learnt to use **qt designer** which is used to build desktop apps without writing code, and `pytube` to interact with YouTube videos and fetch all kinds of info by python.
