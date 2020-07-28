import discord
client = discord.Client()
@client.event
async def on_message(message):
    content = message.content.split(" ")
    if content[0] == "-nuke":
        if content[1][:2] == "<:":
            async for message in message.channel.history(limit=200):
                if content[1] in message.content:
                    await message.delete()
