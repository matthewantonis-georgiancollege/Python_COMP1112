import discord
from discord.ext import commands
import csv
from datetime import datetime
import os

# intents & command prefix declaration
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.messages = True

client = commands.Bot(command_prefix = '!', intents=intents)

# add your Bot Token, Server ID, Channel ID you want the bot to work in goes here...
TOKEN = '???'
GUILD = ???
CHANNEL_ID = ???

# Adding new member to the CSV
def append_to_csv(member_name, join_date):
    # Utility function to append data to the CSV.
    with open('logon.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([member_name, join_date])

# Removing member from the CSV
def remove_from_csv(member_name):
    """Utility function to remove a user from the CSV."""
    rows = []

    # Read the CSV into memory
    with open('logon.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Filter out the user
    rows = [row for row in rows if row[0] != member_name]

    # Write the filtered list back to the CSV
    with open('logon.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

@client.event
# On start up
async def on_ready():

    # use this as help, if you want to change the directory of the csv
    print(os.getcwd())

    # bot ready message
    print("The bot is ready for use!")
    print("----------------------------")

    # Fetch the guild
    guild = client.get_guild(GUILD)

    if not guild:
        print(f"Guild with ID {GUILD} not found.")
        return

    # Fetch members of the guild
    members = guild.members

    if not members:
        print("No members found in the guild.")
        return

    # Current date & time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(datetime.now())

    # Write members to CSV
    try:
        with open('logon.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Join Date'])  # Column headers
            for member in members:
                writer.writerow([member.name, current_time])
            print("CSV file has been created successfully!")
    except Exception as e:
        print(f"Error while writing to CSV: {e}")

@client.event
# member join event
async def on_member_join(member):
    # Current date & time
    join_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Append the new member to the CSV
        append_to_csv(member.name, join_date)
        print(f"{member.name} has been added to the CSV!")
    except Exception as e:
        print(f"Error while adding {member.name} to CSV: {e}")

    # hello message
    channel = client.get_channel(CHANNEL_ID) 
    await channel.send(f"Hello, {member.name}!")

@client.event
# member removed event
async def on_member_remove(member):
    try:
        # Remove the member from the CSV
        remove_from_csv(member.name)
        print(f"{member.name} has been removed from the CSV!")
    except Exception as e:
        print(f"Error while removing {member.name} from CSV: {e}")

    # goodbye message
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f"Goodbye, {member.name}!")

# commands in channel
@client.command()
# !hello command
async def hello(ctx):
    if ctx.channel.id != CHANNEL_ID:  # Check if the command was called in the desired channel
        return  # Exit the function if not in the correct channel
    await ctx.send("Hello, I am Capy!")

@client.command()
# !pullup command
async def pullup(ctx):
    if ctx.channel.id != CHANNEL_ID:  # Check if the command was called in the desired channel
       return # Exit the function if not in the correct channel
    await ctx.send("https://youtu.be/Z67R8nznY28")

client.run(TOKEN)
