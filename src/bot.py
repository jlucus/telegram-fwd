#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import sys
import telebot
import time
from telebot.loop import MessageLoop
from filters import filter_links, filter_hashtags, filter_mentions
from handlers import handle_message
from menu import show_menu

def load_json(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

chats = load_json('data/chats.json')
allowed = set(load_json('data/allowed.json'))
TOKEN = ""
config = load_json('data/config.json')

if 'token' not in config or config['token'] == "":
    sys.exit("No token defined. Define it in the config.json file.")
TOKEN = config['token']

bot = telebot.Bot(TOKEN)

def handle(msg):
    print("Message: " + str(msg))
    if filter_links(msg) or filter_hashtags(msg) or filter_mentions(msg):
        handle_message(msg, chats, allowed, bot)
    elif msg.get('text') == "/menu":
        show_menu(msg['chat']['id'], bot)

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

while True:
    time.sleep(10)