import discord
import responses
from discord.ext import commands



async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTE0NjkzMjIwNjU3MzQ2OTgwNg.GDY2vY.bqSXmP-uQn0JKyC8GSdV3dzBUDI34MQ2yXntaw"
    intents = discord.Intents.default() 
    intents.message_content = True 
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('being a bot')) 
        print(f'{client.user} is now running')

    @client.event 
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # channel_id = 1147012150250975293  
        # channel = client.get_channel(channel_id)
        # if channel:
        #     await channel.send(f"user: {username} \nmassage: {user_message} \nchanel: {channel}")

        if  user_message[0] == "!":
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)