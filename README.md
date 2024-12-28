# Telegram Forward Bot

### telegram-fwd:

├─ data
│   ├── database.json 
│   ├── error.json 
├── src/ 
│   ├── bot.py 
│   ├── access.py 
│   ├── copy_content.py 
│   ├── referral.py 
│   ├── test_bot.py 
├── README.md <-- ** YOU ARE HERE
├── requirements.txt 

## Explanation of Each File and Directory
- data/: This directory contains JSON files used for storing the database and error logs.
- database.json: Stores user data, channel data, and other relevant information.
- error.json: Stores error logs for debugging purposes.
- src/: This directory contains the source code for the bot.
- bot.py: The main script that initializes the bot, handles messages, and runs the bot continuously.
- access.py: Contains functions for granting and checking user access to channels.
- copy_content.py: Contains functions for copying content from channels and preventing infinite looping.
- referral.py: Contains functions for managing the referral system.
- test_bot.py: A test script for checking the bot's functionality with different types of forwarded messages.
- README.md: A markdown file that provides an overview of the project, how to set it up, and how to use it.
- requirements.txt: A file that lists the dependencies required for the project. This can be used to install the necessary packages using pip.

## Features
- Grant access to users based on their UUID or @name.
- Copy content from public channels and prevent infinite looping of reposted content.
- Log errors without stopping the bot.
- Fetch bet information from `gamba.com`.
- Provide a referral system for users.

# Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/telegram-fwd.git
   cd telegram-fwd
2. Install the dependencies:
`pip install -r requirements.txt`
3. Set your Telegram bot token in bot.py:
`TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'`
4. Run the bot:
`python src/bot.py`

# Step 1: Setting Up the Bot
First, we need to set up the bot and ensure it can run continuously. We'll use the telepot library for the bot and requests for fetching data from websites.

# Step 2: Database Setup
We'll use a JSON file to store user data, channel data, and error logs.

# Step 3: Bot Functionality
- Grant Access to Users: We'll manage user access based on their UUID or @name.
- Copy Post Content: The bot will copy content from public channels.
- Prevent Infinite Looping: We'll use a regular expression to detect and post similar content only once.
- Error Logging: Errors will be logged without stopping the bot.
- Referral System: We'll add a referral system for users.
- Fetch Bet Information: The bot will fetch bet information from gamba.com.

# Step 4: Deployment
We'll ensure the bot can be deployed via SSH and run continuously on a web server.

## Implementation
1. Setting Up the Bot

import os
import sys
import json
import telepot
from telepot.loop import MessageLoop
import requests
import re
import time

# Load or create the database
def load_json(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

database_path = os.path.join(data_dir, 'database.json')
error_log_path = os.path.join(data_dir, 'error.json')

database = load_json(database_path)
if 'users' not in database:
    database['users'] = {}
if 'channels' not in database:
    database['channels'] = {}

save_json(database_path, database)

# Initialize the bot
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telepot.Bot(TOKEN)

# Error logging
def log_error(error):
    error_log = load_json(error_log_path)
    error_log.append({"error": str(error)})
    save_json(error_log_path, error_log)

# Function to fetch bet information
def fetch_bet_info(bet_id):
    url = f"https://gamba.com/?modal=bet&type=inhouse&ref={bet_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Parse the response to extract required information
        # This is a placeholder for actual parsing logic
        return response.text
    except requests.RequestException as e:
        log_error(e)
        return f"Error fetching bet information: {e}"

# Function to handle messages
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text']
        if text.startswith('/betid'):
            bet_id = text.split(' ')[1]
            bet_info = fetch_bet_info(bet_id)
            bot.sendMessage(chat_id, bet_info)
        elif text == '/start':
            bot.sendMessage(chat_id, "Welcome to the bot! Use /betid <bet_id> to fetch bet information.")
        # Add more command handling as needed

# Set up the message loop
MessageLoop(bot, handle).run_as_thread()
print("Bot is running...")

# Keep the program running
while True:
    time.sleep(10)
# Grant Access to Users
def grant_access(user_id, channel_id):
    if user_id not in database['users']:
        database['users'][user_id] = {'channels': []}
    if channel_id not in database['users'][user_id]['channels']:
        database['users'][user_id]['channels'].append(channel_id)
    save_json(database_path, database)
def check_access(user_id, channel_id):
    return user_id in database['users'] and channel_id in database['users'][user_id]['channels']
# Copy Post Content and Prevent Infinite Looping
def copy_content(channel_id, content):
if channel_id not in database['channels']:
    database['channels'][channel_id] = {'posts': []}
 if not any(re.search(re.escape(content), post) for post in database['channels'][channel_id]['posts']):
    database['channels'][channel_id]['posts'].append(content)
     save_json(database_path, database)
     return True
  return False
# Referral System
def add_referral(user_id, referred_by):
    if user_id not in database['users']:
        database['users'][user_id] = {'channels': [], 'referred_by': referred_by}
    save_json(database_path, database)
# Fetch Bet Information
Already implemented in the main bot script.

# Deployment
SSH to the server:
`ssh user@yourserver.com`

## Navigate to the project directory:
`cd /path/to/your/project`

## Run the bot:
`python bot.py`
