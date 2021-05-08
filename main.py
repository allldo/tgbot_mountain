import telepot
import sys
import time
from telepot.loop import MessageLoop
import hashlib
TOKEN = '1776437338:AAECu4pNqZKwyabpIcTrOW66kVy3RQG-1RU'
sha = hashlib.sha1(b'1776437338:AAECu4pNqZKwyabpIcTrOW66kVy3RQG-1RU').hexdigest()
print(sha)
f = open('text.txt', 'w')
f.write(sha)
# def startBot(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id)
#
#     if content_type == 'text':
#         bot.sendMessage(chat_id, msg['text'])
#     else:
#         bot.sendMessage(chat_id, "не понимаю")
#
#
# bot = telepot.Bot(TOKEN)
# MessageLoop(bot, startBot).run_as_thread()
# print ('Listening ...')
#
# # Keep the program running.
# while 1:
#     time.sleep(10)
