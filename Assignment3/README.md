# Assignment #3: Discord Bot

## Instructions: 
- When the bot starts for the first time, it should create a list of registered users and add them to a CSV with a date column with the current date & time.
- Each time a user joins the server they should be added with their join date in the date column. 
- Each time a user leaves the server, they should be removed from the CSV.

# How to Use: 
Create a Bot using this guide by [Discord](https://discordpy.readthedocs.io/en/stable/discord.html)
- Make sure to add the bot pic attached and name it Capy. To make it a real Capybara experience
  - Just kidding its only for decoration 
- Add the following permissions (some may not be currently in use)...
  - Read Messages: So the bot can see messages in channels to listen to commands.
  - Send Messages: This allows the bot to send messages like the hello message when someone joins.
  - Manage Messages: This permission might be needed in case the bot needs to delete messages or handle them in a more advanced way in the future (though it isn't currently doing so).
  - View Channel: To ensure the bot can view and interact within specific channels.
  - Read Message History: This might be required for the bot to scan past messages.
  - Access Member List: This permission is necessary to get a list of the members in the on_ready event and other events dealing with members.
  - Monitor Guild's Member Join/Leave: This is necessary to detect when a member joins or leaves the server.

# How It Looks: 
<p align="center">
<img width="400" src="https://github.com/MatthewAntonis/DiscordBot/assets/122380719/c0d86f3d-b93b-4fe8-b953-2eb08307b3f6">
<p/>

## Notes: 
- Created in Pycharm.

### Assignment Due Date: August 11th, 2023
### Mark Received: ???
