import os
import smtplib
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

bdays = {'mummy': '15-07', 'papa': '19-03', 'nannu': '13-01', 'guddu': '06-11', 'sangita-moni': '14-09', 'chote-mausaji': '24-10', 'anita-mony': '12-01', 'bade-mausaji': '24-09', 'bulbul-didi': '08-06', 'rinkal-bhaiya': '28-02', 'tuttu-bhaiya': '14-04', 'siddhu-bhaiya': '12-02', 'tolu-molu': '06-09', 'gudiya': '03-06', 'cherry': '25-06', 'trishabh': '18-08', 'arpit': '27-04', 'vaibhav': '03-01', 'pranav': '03-01', 'harshit': '05-05', 'avi': '24-02', 'yash-chauhan': '11-03', 'ananya': '26-11', 'rushiraj': '01-01', 'hrishabh': '30-07', 'sumit-bhaiya': '13-10', 'mihir': '26-06', 'chayan': '25-09', 'lakshit': '12-02', 'yash-tailor': '08-12', 'goyela': '22-06', 'sid': '11-10', 'parth': '25-07', 'ankit': '23-11', 'kanak': '03-01', 'harsh': '10-12', 'naman': '05-09', 'ghoda': '04-09', 'pranav-hostel': '08-10', 'bhardwaj': '05-08', 'parth-bhaiya': '15-08', 'shubham-hostel': '09-06', 'sanlekh': '04-02', 'princy-didi': '30-11', 'prajjwal': '06-04', 'rakshit': '27-03', 'mridul-bhaiya': '17-07', 'shail': '27-05', 'deep': '01-08', 'shaan': '14-06', 'gagan': '02-07', 'ayush': '13-03', 'jayesh': '05-03', 'atul-bansal': '28-03', 'devesh': '22-10', 'shreyash': '13-09', 'akspa': '28-03', 'vamsi': '19-10', 'ritik': '05-12', 'chirag': '10-06', 'deven': '13-05', 'pulkit': '05-08', 'priyansh': '21-02', 'mahesh': '23-02', 'vipul-mama': '16-11', 'vipul': '21-12', 'sonal': '03-03', 'dev': '06-12', 'ritviz': '02-08', 'aayushi': '22-11', 'shankey-chacha': '18-05', 'ayush-kekri': '29-03'}

anivs = {'mummy-papa': '03-02',
         'sangita-moni': '21-06',
         'anita-moni': '08-05',
         'mama-mami': '24-06',
         'chacha-chachi': '28-11'}

wishes = "Todays's Celebrations\n"
today = datetime.date.today().strftime("%d-%m")

bdays_count = 0
for bday, date in bdays.items():
    if date == today:
        bdays_count += 1

if bdays_count > 0:
    wishes += "Birthdays\n"
    for bday, date in bdays.items():
        if date == today:
            wishes += f"{bday.title()}\n"

anivs_count = 0
for ann, date in anivs.items():
    if date == today:
        anivs_count += 1

if anivs_count > 0:
    wishes += "\nAnniversary:\n"
    for ann, date in anivs.items():
        if date == today:
            wishes += f"{ann.title()}\n"

password = os.getenv("password")

def send_mail(email, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('shivanshsinghal107@gmail.com', password)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('shivanshsinghal107@gmail.com', email, msg)
    print("HEY, EMAIL HAS BEEN SENT!")

    server.quit()

def remind():
    if bdays_count > 0 or anivs_count > 0:
        email = "shivanshsinghal107@gmail.com"
        subject = "Don't forget to wish"
        print(wishes)
        send_mail(email, subject, wishes)
    else:
        print("No Celebrations")


sched = BlockingScheduler()
sched.add_job(remind, 'interval', days = 1)
sched.start()
