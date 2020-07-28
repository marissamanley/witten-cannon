import discord
client = discord.Client()
@client.event
async def on_message(message):
    content = message.content.split(" ")
    if content[0] == "-nuke":
        async for message in message.channel.history(limit=int(content[2])):
            for reaction in message.reactions:
                if reaction.custom_emoji:
                    if reaction.emoji.name == content[1]:
                        await reaction.clear()
client.run('id')
