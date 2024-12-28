# Telegram Bot Project

This project is a Telegram bot designed to collect information from specific Telegram channels or handles. It includes features for filtering links, hashtags, and mentions, as well as a manual post menu for composing messages within the bot.

## Project Structure

```
telegram-bot-project
├── src
│   ├── bot.py          # Main entry point for the Telegram bot
│   ├── filters.py      # Functions to filter messages (links, hashtags, mentions)
│   ├── handlers.py     # Message handling logic for the bot
│   ├── menu.py         # Manual post menu for composing messages
│   └── utils.py        # Utility functions for JSON data handling and formatting
├── data
│   ├── chats.json      # Stores information about monitored channels and handles
│   ├── allowed.json    # List of user IDs allowed to interact with the bot
│   └── config.json     # Configuration settings for the bot
├── requirements.txt     # Dependencies required for the project
└── README.md           # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd telegram-bot-project
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the bot**:
   - Rename `config-sample.json` to `config.json` in the `data` directory.
   - Fill in the required fields, including the bot token.

4. **Run the bot**:
   Execute the following command to start the bot:
   ```
   python src/bot.py
   ```

## Usage Guidelines

- Use commands to interact with the bot, such as adding or removing channels, filtering messages, and composing posts.
- Ensure you are an authorized user by adding your user ID to the `allowed.json` file.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.