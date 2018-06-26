import discord
from discord.ext import commands
#
#
#   Format
# !bot gway #channel name link ======= msg:"@everyone Giveaway Game name : link  " 
#
client = commands.Bot(command_prefix='!bot')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    content = message.content
    
    if content.startswith("!bot"):
        lis=content.split()


        if lis[1] == "gway":
            temp_chan = lis[2]
            channel = client.get_channel(temp_chan[2:len(temp_chan)-1])
            name = lis[3]
            link = lis[4]
            await client.send_message(channel,"@everyone Giveaway Game {} : {} ".format(name,link))
            

client.run("NDYxMjI0ODAwNDcyMjY4ODM1.DhQSow.Rn5POOKonqUfs5CuMxLoH9GUMmY")
