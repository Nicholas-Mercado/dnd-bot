# D&D Bot

A simple Discord bot that retrieves and displays random facts about Dungeons and Dragons (D&D).

## Installation

To use this bot, you will need to have Python 3 installed on your system. You will also need to create a Discord bot token and add it to a .env file in the root directory of this project.

Once you have cloned this repository and added your bot token to the .env file, you can install the required libraries using the pip command:

```
pip install -r requirements.txt
```

## Usage

To run the bot, use the python command in a terminal:

```
python bot.py
```

The bot will connect to Discord and you will be able to use the /fact and /help commands in your Discord server. The /fact command will retrieve and display a random D&D fact, and the /help command will provide instructions on how to use the bot.


## About the Hikari Library

The Hikari library is a simple and lightweight Python library for building Discord bots. It provides an easy-to-use interface for creating and managing Discord bot commands, as well as sending and receiving messages in Discord.

To use the Hikari library, you will need to first create a Discord bot and obtain a bot token. This token will be used to authenticate your bot and allow it to connect to Discord.

Once you have obtained your bot token, you can use it to connect your bot to Discord using the lightbulb.BotApp class in the Hikari library. For example:

from lightbulb import BotApp

```py
TOKEN = "<your bot token here>"

# Create a new bot app and pass the token as an argument
bot = BotApp(token=TOKEN)

# Start the bot
bot.run()
```

Once your bot is connected to Discord, you can use the @bot.command decorator to define commands that your bot can respond to. For example:

```py
@bot.command
@lightbulb.command("hello", "say hello")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond("Hello, world!")
```

In this example, the hello function will be called whenever a user sends a /hello command in Discord. The ctx argument contains information about the command and the Discord channel where it was received. The respond method can be used to send a response back to the Discord channel.

For more information on using the Hikari library, see the [official documentation](<https://lightbulb-bot.readthedocs.io/>

This project is licensed under the MIT License. See the LICENSE file for more information.
