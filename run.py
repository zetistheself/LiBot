import sqlite3
import telebot
from MainThread import MainThread
from SpamThread import Spam
from threading import Thread
from settings import TOKEN


if __name__ == "__main__":
    db = sqlite3.connect('users.sqlite3')
    cur = db.cursor()

    bot = telebot.TeleBot(TOKEN)

    SpamThread = Thread(target=Spam)
    TelebotThread = Thread(target=MainThread)

    SpamThread.start()
    TelebotThread.start()