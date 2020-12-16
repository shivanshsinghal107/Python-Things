import os
import datetime
from telegram.ext import Updater, CommandHandler

bdays = {'name': 'day-month'}
anivs = {}

wishes = "Todays's Celebrations 🎉✨\n\n"
today = datetime.date.today().strftime("%d-%m")

bdays_count = 0
for bday, date in bdays.items():
    if date == today:
        bdays_count += 1

if bdays_count > 0:
    wishes += "Birthdays🎊🍻\n"
    for bday, date in bdays.items():
        if date == today:
            wishes += f"{bday.title()}\n"

anivs_count = 0
for ann, date in anivs.items():
    if date == today:
        anivs_count += 1

if anivs_count > 0:
    wishes += "\nAnniversary❤🤗:\n"
    for ann, date in anivs.items():
        if date == today:
            wishes += f"{ann.title()}\n"


def remind(context):
    if bdays_count > 0 or anivs_count > 0:
        message = wishes
    else:
        message = "No Celebrations"
    context.bot.send_message(chat_id = context.job.context, text = message)

def send_wishes(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "wishes on the way")
    interval = datetime.timedelta(days = 1)
    context.job_queue.run_repeating(remind, interval = interval, first = 0, context = update.effective_chat.id)

def stop_wishes(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Bot Stopped")
    context.job_queue.stop()


def main():
    TOKEN = os.getenv("TOKEN")
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', send_wishes))
    dp.add_handler(CommandHandler('stop', stop_wishes))
    PORT = int(os.environ.get('PORT', 5000))
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://example.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
