import telebot
from telebot import types
import sqlite3
import json
from settings import phrase_settings, buttons_text, reply_text, TOKEN


bot = telebot.TeleBot(TOKEN)


def MainThread():
    @bot.message_handler(commands=['start'])
    def welcome(message):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(buttons_text["Receive notificatoins on"], callback_data='receive_notificatoins_on'))
        reply_text = reply_text["Welcome text"]
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
                reply_text = reply_text["Receive notificatoins on text"]
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(buttons_text["Receive notificatoins off"], callback_data='receive_notificatoins_off'))
                bot.send_message(call.message.chat.id, reply_text, reply_markup=markup)
                cur.execute(f"""INSERT INTO USERS(ID) VALUES({call.message.chat.id})""")
                db.commit()
            else:
                bot.answer_callback_query(callback_query_id=call.id, text='Вы уже учавствуете в оценке блюд!', show_alert=True)
            
        elif call.data == 'receive_notificatoins_off':
            db = sqlite3.connect('users.sqlite3')
            cur = db.cursor()   
            cur.execute(f"""DELETE FROM USERS WHERE ID='{call.message.chat.id}'""")
            db.commit()
            reply_text = reply_text["Receive notificatoins off text"]
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(buttons_text["Receive notificatoins on"], callback_data='receive_notificatoins_on'))
            bot.send_message(call.message.chat.id, reply_text, reply_markup=markup)
        else:
            db2 = sqlite3.connect('stats.sqlite3')
            cur2 = db2.cursor()
            data = json.loads(call.data)
            day = 'D' + ''.join(str(data['date']).split('-'))
            if data['meal'] == 'breakfast':
                cur2.execute(f"""SELECT breakfast FROM {day} WHERE ID = '{call.message.chat.id}'""")
                cort = cur2.fetchall()
                if cort == [] or cort == [(None,)] or cort == [(None,), (None,)]:
                    cur2.execute(f"""INSERT INTO {day} VALUES({data['mark']}, NULL, NULL, {call.message.chat.id})""")
                    db2.commit()
                    bot.answer_callback_query(callback_query_id=call.id, text=phrase_settings["Acceptance of vote phrase"], show_alert=True)
                    print(data['date'], data['mark'])
                else:
                    bot.answer_callback_query(callback_query_id=call.id, text=phrase_settings["Voice failure phrase"], show_alert=True)
                    print('decline')
            if data['meal'] == 'lunch':
                cur2.execute(f"""SELECT lunch FROM {day} WHERE ID = '{call.message.chat.id}'""")
                cort = cur2.fetchall()
                if cort == [] or cort == [(None,)] or cort == [(None,), (None,)]:
                    cur2.execute(f"""INSERT INTO {day} VALUES(NULL, {data['mark']}, NULL, {call.message.chat.id})""")
                    db2.commit()
                    bot.answer_callback_query(callback_query_id=call.id, text=phrase_settings["Acceptance of vote phrase"], show_alert=True)
                    print(data['date'], data['mark'])
                else:
                    bot.answer_callback_query(callback_query_id=call.id, text=phrase_settings["Voice failure phrase"], show_alert=True)
                    print('decline')
            if data['meal'] == 'dinner':
                cur2.execute(f"""SELECT dinner FROM {day} WHERE ID = '{call.message.chat.id}'""")
                cort = cur2.fetchall()
                if cort == [] or cort == [(None,)] or cort == [(None,), (None,)]:
                    cur2.execute(f"""INSERT INTO {day} VALUES(NULL, NULL, {data['mark']}, {call.message.chat.id})""")
                    db2.commit()
                    bot.answer_callback_query(callback_query_id=call.id, text=phrase_settings["Acceptance of vote phrase"], show_alert=True)
                    print(data['date'], data['mark'])
                else:
                    print(cort)
                    bot.answer_callback_query(callback_query_id=call.id, text=phrase_settings["Voice failure phrase"], show_alert=True)
                    print('decline')


    bot.infinity_polling()