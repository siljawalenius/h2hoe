#add all possible drink water quotes 
DRINK_WATER = [
    "You look parched 💧",
    "Looks like you could use some water 🌊",
    "💦 💦 💦",
    "Stop being so thirsty and drink some water already 🙄 🌊",
    "Is that the Sahara Desert? Nope. Just ur dry ass skin. Drink ur water 🥤",
    "It's water time bish 🥤",
    "🌊 🌊 🌊",
    "Your life will be better if you drink water 🧊",
    "Put down the dumb bish juice and pick up your water bottle 💧",
    "It's water time!!! 🌧 🌧 🌧",
    "Someone's thirsty 😏 🥤"
]

from twilio.rest import Client
import os
import schedule
import time
import random
#from twilio_creds import cell_num, twilio_num, account_sid, token


cell_num=os.environ['CELLNUM']
twilio_num=os.environ['TWILIONUM']
account_sid=os.environ['ACCOUNTSID']
token=os.environ['TOKEN']



num_quotes = len(DRINK_WATER)-1

def send_text(all_texts = DRINK_WATER):
    client = Client(account_sid, token)
    quote = all_texts[random.randint(0, num_quotes)]
    message = client.messages.create( to=cell_num, from_=twilio_num, body=quote)
    print(message.sid)

# send_text(DRINK_WATER)
schedule.every().day.at("23:01").do(send_text,DRINK_WATER)

#schedule a text every hour between 8 and 5
#array of hours to send a text
hours = ["08:00", "09:00","09:30","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"]

for hour in hours:
    schedule.every().day.at(hour).do(send_text,DRINK_WATER)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)