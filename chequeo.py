import telebot
import time
import telegram
from telegram.ext import *

#configuraciones del bot

TOKEN = '1156537678:AAG9MWA6APVAjfODTVZDovFbTr11dW-LtwU'
chat_id = '805954751'

text = 'Anda a crash'
def mandarBot(TOKEN,chat_id):
    tb = telebot.TeleBot(token=TOKEN)
    tb.send_message(chat_id,text )
    time.sleep(10)
