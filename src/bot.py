import os
import sys
import json
import telepot

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
config = load_json('data/config.json')

if 'token' not in config or config['token'] == "":
    sys.exit("No token defined. Define it in the config.json file.")
TOKEN = config['token']

try:
    bot = telepot.Bot(TOKEN)
except Exception as e:
    sys.exit(f"Failed to initialize bot: {e}")

def handle(msg):
    print("Message: " + str(msg))
    if filter_links(msg) or filter_hashtags(msg) or filter_mentions(msg):
        # Add your message handling logic here
        pass

# Example function to test bot connection
def test_bot():
    try:
        bot.getMe()
        print("Bot initialized successfully.")
    except Exception as e:
        sys.exit(f"Failed to communicate with Telegram API: {e}")

# Test the bot connection
test_bot()