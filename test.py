from telebot import types
import telebot
import sqlite3
from threading import Thread
import schedule


TOKEN = "6931954722:AAHcZ8wGDw3uE81pBDrV2Bmwfx2_W5F-4rw"

db = sqlite3.connect('users.sqlite3')
cur = db.cursor()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Получать Уведомления', callback_data='receive_notificatoins_on'))
    reply_text = 'GHbdtn'
    bot.send_message(message.chat.id, reply_text, reply_markup=markup)


@bot.callback_query_handler(func= lambda call: True)
def answ(call):
    if call.data == 'receive_notificatoins_on':
        db = sqlite3.connect('users.sqlite3')
        cur = db.cursor()
        cur.execute("""SELECT ID FROM USERS""")
        users = []
        for user in cur.fetchall():
            users.append(user[0])

        if str(call.message.chat.id) not in users:
            reply_text = 'ЩЛ'
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Не получать Уведомления', callback_data='receive_notificatoins_off'))
            bot.send_message(call.message.chat.id, reply_text, reply_markup=markup)
            cur.execute(f"""INSERT INTO USERS(ID) VALUES({call.message.chat.id})""")
            db.commit()
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Вы уже учавствуете в оценке блюд!', show_alert=True)
        
    if call.data == 'receive_notificatoins_off':
        db = sqlite3.connect('users.sqlite3')
        cur = db.cursor()
        cur.execute(f"""DELETE FROM USERS WHERE ID='{call.message.chat.id}'""")
        db.commit()
    

bot.infinity_polling()
