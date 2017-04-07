import time
import random
import datetime
import telepot
import urllib2
import socket
import socks
import json

#Welcome to TOR
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150)
socket.socket = socks.socksocket

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print  'Got command: %s' % command

    if command == '/usd':
        resp = urllib2.urlopen ('https://btc-e.com/api/3/ticker/ltc_usd') 
        data = json.load (resp)
        bot.sendMessage(chat_id, 'High price: ' + str(data['ltc_usd']['high']) + '\n' 
        + 'Low price: '+str(data['ltc_usd']['low']) + '\n'
        + 'Avg price: '+str(data['ltc_usd']['avg']) + '\n'
        + 'Buy price: '+str(data['ltc_usd']['buy']) + '\n'
        + 'Sell price: '+str(data['ltc_usd']['sell']) + '\n')
 
    elif command == '/rub':
        resp = urllib2.urlopen ('https://btc-e.com/api/3/ticker/ltc_rur') 
        data = json.load (resp)
        bot.sendMessage(chat_id, 'High price: ' + str(data['ltc_rur']['high']) + '\n' 
        + 'Low price: '+str(data['ltc_rur']['low']) + '\n'
        + 'Avg price: '+str(data['ltc_rur']['avg']) + '\n'
        + 'Buy price: '+str(data['ltc_rur']['buy']) + '\n'
        + 'Sell price: '+str(data['ltc_rur']['sell']) + '\n')
 

bot = telepot.Bot('')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
