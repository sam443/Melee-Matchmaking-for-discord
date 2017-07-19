##  Melee matchmaking bot ##
##						  ##
##						  ##
##						  ##
##  Resources:            ##
##						  ##
## https://tutorials.botsfloor.com/creating-chatbots-for-discord-90407e1bf382

import database #user database
import secrets  #bot token, id and secret.
import discord
from discord.ext.commands import Bot


#all bot commands will begin with "!"
mm_bot = Bot(command_prefix="!")

@mm_bot.event
async def on_read():
    print("Client logged in")


#typing !hello will trigger this.
@mm_bot.command()
async def hello(*args):
    return await mm_bot.say("What's up, ")

@mm_bot.command()
async def register(*args):
	user = ''
	print("args: ", args)

	message = "User registered (not really tho, database not implimented yet ;) \n full message: " + str(args) + "\n Args[1]: " + str(args[1])
	return await mm_bot.say(message)







#initializing database
database.db_init()
#Starting bot
mm_bot.run(secrets.bot_token)