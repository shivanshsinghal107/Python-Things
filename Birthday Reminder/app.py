import os
import datetime
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

account_sid = os.getenv('sid')
auth_token = os.getenv('token')
client = Client(account_sid, auth_token)

bdays = {'name': 'day-month'}

anivs = {}

wishes = "Todays's Celebrations 🎉✨ "
today = datetime.date.today().strftime("%d-%m")

bdays_count = 0
for bday, date in bdays.items():
    if date == today:
        bdays_count += 1

if bdays_count > 0:
    wishes += "Birthdays🎊🍻: "
    for bday, date in bdays.items():
        if date == today:
            wishes += f"{bday.title()} | "
    wishes = wishes[:-2]

anivs_count = 0
for ann, date in anivs.items():
    if date == today:
        anivs_count += 1

if anivs_count > 0:
    wishes += "Anniversary❤🤗: "
    for ann, date in anivs.items():
        if date == today:
            wishes += f"{ann.title()} | "
    wishes = wishes[:-2]

def remind():    
    if anivs_count > 0 or bdays_count > 0:
        message = client.messages.create(
                                            from_='whatsapp:+14155238886',  
                                            body = wishes,      
                                            to = 'whatsapp:your_no'
                                        )
        print(message.sid)
    else:
        print("No celebrations")


sched = BlockingScheduler(timezone = "Asia/Kolkata")
sched.add_job(remind, 'interval', days = 1, start_date = "2020-12-08 00:01:01")

sched.start()
