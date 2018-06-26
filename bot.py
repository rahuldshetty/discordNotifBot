import discord
import random
from discord.ext import commands
#
#
#   Format
# !bot gway #channel name link ======= msg:"@everyone Giveaway Game name : link  " 
# !bot random begin last
client = commands.Bot(command_prefix='!bot')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    content = message.content
    
    if content.startswith("!bot"):
        lis=content.split()

        if lis[1] == "random":
            f=int(lis[2])
            s=int(lis[3])
            channel = message.channel
            await client.send_message(channel,"Random Number : {} ".format(random.randint(f,s)))

        if lis[1] == "gway":
            temp_chan = lis[2]
            channel = client.get_channel(temp_chan[2:len(temp_chan)-1])
            name = ""
            for i in range(3,len(lis)-1):
                name = name + " " + lis[i]
            link = lis[len(lis)-1]
            await client.send_message(channel,"@everyone Giveaway Game {} : {} ".format(name,link))
            

client.run("NDYxMjI0ODAwNDcyMjY4ODM1.DhQSow.Rn5POOKonqUfs5CuMxLoH9GUMmY")
