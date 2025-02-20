# Discord Bot Documentation

## Disclaimer
This bot is created strictly for **educational purposes only**. The author is not liable for any damage caused by the misuse of this bot. Using this bot for illegal activities, including but not limited to server raids, harassment, or unauthorized access, is **strictly forbidden**. By using this bot, you agree to take full responsibility for your actions and ensure compliance with all applicable laws and Discord's Terms of Service.

---

## Overview
This bot is designed to demonstrate advanced interactions with Discord's API using Python's `discord.py` library. It includes commands for server management, such as renaming servers, banning members, creating/deleting channels, and spamming messages. These functionalities are intended to simulate scenarios for educational purposes, such as learning about bot development, server moderation, and API usage.

---

## Features
1. Server Nuke Command (`!nuke`)
   - Renames the server.
   - Bans all members except those with excluded roles or authorized users.
   - Creates spam channels and sends spam messages.
   - Deletes all existing channels.
   - Logs detailed information about the operation.

2. Server Cleanup Command (`!cleanall`)
   - Resets the server name to "Cleaned Server."
   - Deletes all existing channels.
   - Creates a new channel named "cleaned" to indicate completion.

3. Security Features
   - Commands can only be executed by authorized users (specified in `AUTHORIZED_USERS`).
   - Excludes specific roles from being banned/kicked (specified in `EXCLUDED_ROLES`).
   - Logs all operations for transparency and debugging.

4. Logging
   - Logs all critical events, errors, and intents to a file (`bot.log`) and console.

---

## Workflow
### 1. Initialization
- The bot initializes with specific intents enabled (`guilds`, `members`, `messages`, etc.) to interact with Discord's API.
- It checks the environment variable `DISCORD_TOKEN` for authentication.
- Upon startup, it logs all enabled intents for verification.

### 2. Authorization
- Only users listed in the `AUTHORIZED_USERS` array can execute commands.
- Members with roles specified in `EXCLUDED_ROLES` are protected from bans/kicks.

### 3. Commands
#### `!nuke`
1. Server Rename: Changes the server name to `GUILD_NAME`.
2. Ban Members: Iterates through all members and bans those who:
   - Are not bots.
   - Do not have excluded roles.
   - Are not in the `AUTHORIZED_USERS` list.
3. Create Spam Channels: Creates multiple text channels (`CHANNEL_NAME`) and sends spam messages (`SPAM_MESSAGE`) in each.
4. Delete Channels: Deletes all existing channels except the newly created spam channels.
5. Log Results: Sends a summary of the operation, including the number of banned members, spam channels created, and time taken.

#### `!cleanall`
1. Reset Server Name: Changes the server name to "Cleaned Server."
2. Delete Channels: Deletes all existing channels.
3. Create Cleaned Channel: Creates a new channel named "cleaned" and sends a confirmation message.
4. Log Results: Sends a summary of the cleanup operation.

---

## Usage
1. Prerequisites:
   - Python 3.8 or higher.
   - Install dependencies:
     ```
     pip install discord.py python-dotenv
     ```

2. Configuration:
   - Create a `.env` file in the project directory:
     ```
     DISCORD_TOKEN=your_discord_bot_token_here
     ```
   - Update the following variables in the code:
     - `AUTHORIZED_USERS`: Add your Discord user ID(s).
     - `EXCLUDED_ROLES`: Add role names to exclude from bans/kicks.

3. Run the Bot:

---

## Educational Purpose
This bot serves as a learning tool for:
- Understanding Discord API interactions.
- Exploring bot development with `discord.py`.
- Simulating server management scenarios.
- Learning about security best practices in bot development.

---

## Legal Notice
The author does not condone or support any malicious use of this bot. Any harm caused by misuse of this bot is the sole responsibility of the user. Always ensure compliance with Discord's Terms of Service and local laws.

---

## Contributions
If you find this project useful, feel free to contribute by:
- Reporting bugs or issues.
- Suggesting improvements.
- Adding new features (with proper documentation).

---

By adhering to the guidelines above, you can safely use this bot for educational purposes while ensuring the security of both the bot and its users.
