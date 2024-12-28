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
        json.dump(data, f, indent=4)

# Ensure the data directory exists
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Ensure the config file exists
config_path = os.path.join(data_dir, 'config.json')
if not os.path.isfile(config_path):
    with open(config_path, 'w') as f:
        json.dump({}, f)

chats = load_json(os.path.join(data_dir, 'chats.json'))
allowed = set(load_json(os.path.join(data_dir, 'allowed.json')))
config = load_json(config_path)

# Debug statement to check if config is loaded correctly
print("Config loaded:", config)

if 'token' not in config or config['token'] == "":
    token = input("Enter your Telegram bot token: ")
    config['token'] = token
    save_json(config_path, config)
    print("Token saved to config.json")
else:
    token = config['token']

# Debug statement to check if token is retrieved correctly
print("Token retrieved:", token)

try:
    bot = telepot.Bot(token)
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

# Delete webhook if it exists
try:
    bot.deleteWebhook()
    print("Webhook deleted successfully.")
except Exception as e:
    print(f"Failed to delete webhook: {e}")

# Main bot operation logic
print("Bot is running...")

# Add your main bot logic here
# For example, you can set up message handling
bot.message_loop(handle)

# Keep the program running
while True:
    pass