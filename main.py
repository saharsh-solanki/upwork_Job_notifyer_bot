import random

import telebot
import time
import Scraper

obj = Scraper.UpworkScraper()
import os

Bot_Token = os.environ.get("BOT_TOKEN")
# Bot_Token = "5365649147:AAFGLeILBN6xmwLvqN_l31EfRniGFOkc-Ig"

bot = telebot.TeleBot(Bot_Token, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN

user_dict = {}


class User:
    def __init__(self, mobile_number):
        self.mobile_number = mobile_number
        self.cookie = None


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text_to_send = "Hey Welcome !\n Bot Is Created By Saharsh Solanki \n Get Notified When a New Client Post A JOB \n Please Enter Your Coookie"
    print("Sended !!")
    bot.register_next_step_handler(bot.send_message(message.chat.id, text_to_send), process_mobile_number_step)


def process_mobile_number_step(message):
    chat_id = message.chat.id
    try:
        obj.cookie_data = message.text
        check = obj.FetchJobs()
        if check:
            msg = bot.reply_to(message,
                               'Hey Cookie Is Correct You Will Get Notified of every Job POST')
            bot.register_next_step_handler(bot.send_message(message.chat.id, "Hey Type 'OK'"), proccess_job)
        else:
            ms = bot.send_message(chat_id, "Please Enter valid cookie ")
            bot.register_next_step_handler(ms, process_mobile_number_step)
    except Exception as e:
        ms = bot.send_message(chat_id, "Please Enter valid cookie ")
        bot.register_next_step_handler(ms, process_mobile_number_step)


def proccess_job(message):
    chat_id = message.chat.id
    check = message.text
    all_jobs = []
    fetched = obj.FetchJobs()
    run = True
    try:
        while run:

            try:
                if fetched == False:
                    return False
                jobs = fetched["results"]
                send = False
                for i in jobs:
                    if i["title"] not in all_jobs:
                        title = i['title'] if "title" in i else ""
                        description = i["description"]  if "description" in i else ""
                        payment_text = "Not Verified"
                        budget = 0
                        if "client" in i:
                            if "totalSpent" in i["client"]:
                                if i["client"]["totalSpent"] > 0:
                                    payment_text = "Verified Client and Total Spent of client is "+str(i["client"]["totalSpent"])
                                else:
                                    payment_text = "can't verify client's payment "
                            else:
                                payment_text = "can't verify client's payment "
                        try:
                            if "amount" in i:
                                budget = i['amount']["amount"]
                        except:
                            pass

                        messgae = f" JOB NUMBER :- {len(all_jobs) + 1} \n New Got Arrived : - {title} \n Job Description:- { description } \n Payment : {payment_text} \n Client's Budget : ${budget} "
                        bot.send_message(chat_id, messgae)
                        all_jobs.append(i["title"])
                        send = True

                    else:
                        pass
                if send:
                    bot.send_message(chat_id,
                                     "I Am Waiting And When a new Job in posted i will message you so relax and please on notification of dekstop !")
                wait = random.randint(60,120)
                time.sleep(wait)
            except Exception as e:
                print("got some error!!")
                print(e)
    except:
        bot.send_message(chat_id, "Cookie Expired Try Again")


while True:
    try:
        bot.polling()
    except:
        time.sleep(10)
