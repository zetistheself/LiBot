from telebot import types
import sqlite3
import schedule
import json
import datetime
import telebot
from settings import time_settings, phrase_settings, TOKEN


bot = telebot.TeleBot(TOKEN)


def Spam():
    schedule.every().day.at(time_settings["Breakfast time"]).do(send_spam_message_breakfast) 
    schedule.every().day.at(time_settings["Lunch time"]).do(send_spam_message_lunch)
    schedule.every().day.at(time_settings["Dinner time"]).do(send_spam_message_dinner)

    while True:
        schedule.run_pending()


def send_spam_message_lunch():
    db = sqlite3.connect('users.sqlite3')
    cur = db.cursor()

    cur.execute("""SELECT ID FROM USERS""")
    u_users = cur.fetchall()
    users = []
    for n in u_users:
        users.append(n)

    date = str(datetime.datetime.now().strftime('%Y-%m-%d'))

    for user_id in range(len(users)):
        mark1 = {'date': date, 'meal': 'lunch', 'mark': '1'}
        mark1_json = json.dumps(mark1)

        mark2 = {'date': date, 'meal': 'lunch', 'mark': '2'}
        mark2_json = json.dumps(mark2)

        mark3 = {'date': date, 'meal': 'lunch', 'mark': '3'}
        mark3_json = json.dumps(mark3)

        mark4 = {'date': date, 'meal': 'lunch', 'mark': '4'}
        mark4_json = json.dumps(mark4)
        
        mark5 = {'date': date, 'meal': 'lunch', 'mark': '5'}
        mark5_json = json.dumps(mark5)

        mark6 = {'date': date, 'meal': 'lunch', 'mark': '6'}
        mark6_json = json.dumps(mark6)

        mark7 = {'date': date, 'meal': 'lunch', 'mark': '7'}
        mark7_json = json.dumps(mark7)

        mark8 = {'date': date, 'meal': 'lunch', 'mark': '8'}
        mark8_json = json.dumps(mark8)

        mark9 = {'date': date, 'meal': 'lunch', 'mark': '9'}
        mark9_json = json.dumps(mark9)

        mark10 = {'date': date, 'meal': 'lunch', 'mark': '10'}
        mark10_json = json.dumps(mark10)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('1', callback_data=mark1_json), types.InlineKeyboardButton('2', callback_data=mark2_json), types.InlineKeyboardButton('3', callback_data=mark3_json), types.InlineKeyboardButton('4', callback_data=mark4_json), types.InlineKeyboardButton('5', callback_data=mark5_json))
        markup.add(types.InlineKeyboardButton('6', callback_data=mark6_json), types.InlineKeyboardButton('7', callback_data=mark7_json), types.InlineKeyboardButton('8', callback_data=mark8_json), types.InlineKeyboardButton('9', callback_data=mark9_json), types.InlineKeyboardButton('10', callback_data=mark10_json))
        bot.send_message(users[user_id][0], phrase_settings["Lunch phrase"], reply_markup=markup)


def send_spam_message_breakfast():
    db = sqlite3.connect('users.sqlite3')
    cur = db.cursor()

    cur.execute("""SELECT ID FROM USERS""")
    u_users = cur.fetchall()
    users = []
    for n in u_users:
        users.append(n)

    db2 = sqlite3.connect('stats.sqlite3')
    cur2 = db2.cursor()

    cur2.execute(f"""CREATE TABLE IF NOT EXISTS D{''.join(str(datetime.datetime.now().strftime('%Y-%m-%d')).split('-'))} (breakfast TEXT, lunch TEXT, dinner TEXT, ID TEXT)""")
    db2.commit()

    date = str(datetime.datetime.now().strftime('%Y-%m-%d'))

    

    for user_id in range(len(users)):
        mark1 = {'date': date, 'meal': 'breakfast', 'mark': '1'}
        mark1_json = json.dumps(mark1)

        mark2 = {'date': date, 'meal': 'breakfast', 'mark': '2'}
        
        mark2_json = json.dumps(mark2)

        mark3 = {'date': date, 'meal': 'breakfast', 'mark': '3'}
        mark3_json = json.dumps(mark3)

        mark4 = {'date': date, 'meal': 'breakfast', 'mark': '4'}
        mark4_json = json.dumps(mark4)
        
        mark5 = {'date': date, 'meal': 'breakfast', 'mark': '5'}
        mark5_json = json.dumps(mark5)

        mark6 = {'date': date, 'meal': 'breakfast', 'mark': '6'}
        mark6_json = json.dumps(mark6)

        mark7 = {'date': date, 'meal': 'breakfast', 'mark': '7'}
        mark7_json = json.dumps(mark7)

        mark8 = {'date': date, 'meal': 'breakfast', 'mark': '8'}
        mark8_json = json.dumps(mark8)

        mark9 = {'date': date, 'meal': 'breakfast', 'mark': '9'}
        mark9_json = json.dumps(mark9)

        mark10 = {'date': date, 'meal': 'breakfast', 'mark': '10'}
        mark10_json = json.dumps(mark10)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('1', callback_data=mark1_json), types.InlineKeyboardButton('2', callback_data=mark2_json), types.InlineKeyboardButton('3', callback_data=mark3_json), types.InlineKeyboardButton('4', callback_data=mark4_json), types.InlineKeyboardButton('5', callback_data=mark5_json))
        markup.add(types.InlineKeyboardButton('6', callback_data=mark6_json), types.InlineKeyboardButton('7', callback_data=mark7_json), types.InlineKeyboardButton('8', callback_data=mark8_json), types.InlineKeyboardButton('9', callback_data=mark9_json), types.InlineKeyboardButton('10', callback_data=mark10_json))
        bot.send_message(users[user_id][0], phrase_settings["Breakfast phrase"], reply_markup=markup)


def send_spam_message_dinner():
    db = sqlite3.connect('users.sqlite3')
    cur = db.cursor()

    cur.execute("""SELECT ID FROM USERS""")
    u_users = cur.fetchall()
    users = []
    for n in u_users:
        users.append(n)

    date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    
    for user_id in range(len(users)):
        mark1 = {'date': date, 'meal': 'dinner', 'mark': '1'}
        mark1_json = json.dumps(mark1)

        mark2 = {'date': date, 'meal': 'dinner', 'mark': '2'}
        mark2_json = json.dumps(mark2)

        mark3 = {'date': date, 'meal': 'dinner', 'mark': '3'}
        mark3_json = json.dumps(mark3)

        mark4 = {'date': date, 'meal': 'dinner', 'mark': '4'}
        mark4_json = json.dumps(mark4)
        
        mark5 = {'date': date, 'meal': 'dinner', 'mark': '5'}
        mark5_json = json.dumps(mark5)

        mark6 = {'date': date, 'meal': 'dinner', 'mark': '6'}
        mark6_json = json.dumps(mark6)

        mark7 = {'date': date, 'meal': 'dinner', 'mark': '7'}
        mark7_json = json.dumps(mark7)

        mark8 = {'date': date, 'meal': 'dinner', 'mark': '8'}
        mark8_json = json.dumps(mark8)

        mark9 = {'date': date, 'meal': 'dinner', 'mark': '9'}
        mark9_json = json.dumps(mark9)

        mark10 = {'date': date, 'meal': 'dinner', 'mark': '10'}
        mark10_json = json.dumps(mark10)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('1', callback_data=mark1_json), types.InlineKeyboardButton('2', callback_data=mark2_json), types.InlineKeyboardButton('3', callback_data=mark3_json), types.InlineKeyboardButton('4', callback_data=mark4_json), types.InlineKeyboardButton('5', callback_data=mark5_json))
        markup.add(types.InlineKeyboardButton('6', callback_data=mark6_json), types.InlineKeyboardButton('7', callback_data=mark7_json), types.InlineKeyboardButton('8', callback_data=mark8_json), types.InlineKeyboardButton('9', callback_data=mark9_json), types.InlineKeyboardButton('10', callback_data=mark10_json))
        bot.send_message(users[user_id][0], phrase_settings["Dinner phrase"], reply_markup=markup)

