import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive
from dotenv import load_dotenv
import os
import random
import time

#-----SETUP-----#import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive
from dotenv import load_dotenv

import os

#-----SETUP-----#

prefix = ">"

#use the .env feature to hide your token
load_dotenv()

keep_alive()
token = os.getenv("TOKEN")
print(f"Token loaded: {token is not None}")
if token is None:
    print("ERROR: TOKEN not found in environment variables!")
    exit(1)

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)



@bot.command()
async def help(ctx):
    await ctx.send(
        f"**Help AutoOwO**\n"
        f"**{prefix}autoOwO** - owoh, owo sell all, owo flip 500 and owo cash 50 seconds.\n"
        f"**{prefix}stopautoOwO** - stops autoOwO.\n"
        f"**{prefix}banbypass** - Prevents banning by taking breaks.\n"
        "Example: the bot takes breaks (5 min, 10 min, 15 min, etc.)\n"
        "Made by Vicky | Support: https://discord.gg/Vd48FAZCGV"
    )


import random
import time

# Command usage statistics
cmd_stats = {
    'owoh': 0,
    'sell': 0,
    'flip': 0,
    'cash': 0,
    'hunt': 0,
    'battle': 0,
    'pray': 0
}
last_pray_time = 0

@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO is now **enabled**!')
    global dmcs, last_pray_time
    dmcs = True
    cycle_count = 0
    while dmcs:
        async with ctx.typing():
            # Randomize delays for human-like behavior
            delay1 = random.randint(4, 8)
            await asyncio.sleep(delay1)
            await ctx.send('owoh')
            cmd_stats['owoh'] += 1
            print(f"{Fore.GREEN}succefully owoh")

            # Auto hunt
            delay2 = random.randint(2, 5)
            await asyncio.sleep(delay2)
            await ctx.send('owo hunt')
            cmd_stats['hunt'] += 1
            print(f"{Fore.GREEN}succefully hunt")

            # Auto battle
            delay3 = random.randint(2, 5)
            await asyncio.sleep(delay3)
            await ctx.send('owo battle')
            cmd_stats['battle'] += 1
            print(f"{Fore.GREEN}succefully battle")

            # Sell all
            delay4 = random.randint(8, 15)
            await asyncio.sleep(delay4)
            await ctx.send('owo sell all')
            cmd_stats['sell'] += 1
            print(f"{Fore.GREEN}succefully sell")

            # Flip
            await ctx.send('owo flip 500')
            cmd_stats['flip'] += 1
            print(f"{Fore.GREEN}succefully owo flip 500")

            # Cash
            delay5 = random.randint(8, 15)
            await asyncio.sleep(delay5)
            await ctx.send('owo cash')
            cmd_stats['cash'] += 1
            print(f"{Fore.GREEN}succefully cash")

            # Auto pray every 10 minutes
            now = time.time()
            if now - last_pray_time > 600:
                await ctx.send('owo pray')
                cmd_stats['pray'] += 1
                last_pray_time = now
                print(f"{Fore.GREEN}succefully pray")

            # Every 5 cycles, check inventory and use all gems
            cycle_count += 1
            if cycle_count % 5 == 0:
                await ctx.send('owo inv')
                print(f"{Fore.GREEN}Checking inventory for gems...")
                await asyncio.sleep(5)  # Wait for OwO bot to reply
                # Gems will be used by the on_message event below

            # Final random sleep before next cycle
            await asyncio.sleep(random.randint(10, 18))

# List of gem keywords as they appear in OwO inventory
GEM_KEYWORDS = [
    'Luck', 'Huntbot', 'Trap', 'Gem', 'Magic', 'Crate', 'Lootbox', 'Weapon', 'Cowoncy', 'Developer', 'Daily', 'Exp', 'Hidden', 'Special', 'Patreon'
]

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # Only process messages from OwO Bot
    if str(message.author.id) not in ["1202830963034296360", "1202830963034296360"]:  # OwO Bot IDs
        return
    if "Inventory" in message.content or "gem" in message.content.lower():
        # Try to extract all gem names from the embed (if present)
        if hasattr(message, 'embeds') and message.embeds:
            embed = message.embeds[0]
            description = embed.description if embed.description else ''
            for gem in GEM_KEYWORDS:
                if gem.lower() in description.lower():
                    # Use the gem (send owo use <gem>)
                    channel = message.channel
                    await channel.send(f'owo use {gem}')
                    print(f"{Fore.GREEN}Attempted to use gem: {gem}")


@bot.command()
async def stats(ctx):
    msg = (
        f"**AutoOwO Stats:**\n"
        f"owoh: {cmd_stats['owoh']}\n"
        f"hunt: {cmd_stats['hunt']}\n"
        f"battle: {cmd_stats['battle']}\n"
        f"sell: {cmd_stats['sell']}\n"
        f"flip: {cmd_stats['flip']}\n"
        f"cash: {cmd_stats['cash']}\n"
        f"pray: {cmd_stats['pray']}"
    )
    await ctx.send(msg)

@bot.command()
async def stopautoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO Magi is now **disabled**!')
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def banbypass(ctx):
    await ctx.message.delete()
    await ctx.send('banbypass is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell c')
            print(f"{Fore.GREEN}succefully sell c")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(15)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(300) 

            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(4)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(900)

            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(4)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(900)

            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(15)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(1200)        
            
# @bot.command()
# async def stopautoOwO(ctx):
#     await ctx.message.delete()
#     await ctx.send('auto OwO Magi is now **disabled**!')
#     global dmcs
#     dmcs = False


@bot.event
async def on_ready():
    activity = discord.Game(name="DM for help", type=4)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

░█████╗░██╗░░░██╗████████╗░█████╗    ░░█████╗░░██╗░░░░░░░██╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗    ██╔══██╗░██║░░██╗░░██║██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║    ██║░░██║░╚██╗████╗██╔╝██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║    ██║░░██║░░████╔═████║░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝    ╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝    ░░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░


selfbot is ready!
''')


keep_alive()
try:
    bot.run(token)
except Exception as e:
    print(f"Error running bot: {e}")
    import traceback
    traceback.print_exc()

prefix = ">"

#use the .env feature to hide your token
load_dotenv()

keep_alive()
token = os.getenv("TOKEN")
print(f"Token loaded: {token is not None}")
if token is None:
    print("ERROR: TOKEN not found in environment variables!")
    exit(1)

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

# Command usage statistics
cmd_stats = {
    'owoh': 0,
    'sell': 0,
    'flip': 0,
    'cash': 0,
    'hunt': 0,
    'battle': 0,
    'pray': 0
}
last_pray_time = 0

@bot.command()
async def help(ctx):
    await ctx.send(
        f"**Help AutoOwO**\n"
        f"**{prefix}autoOwO** - owoh, smart sell (no g,m,l,e animals), owo flip 500 and owo cash with auto gem usage.\n"
        f"**{prefix}stopautoOwO** - stops autoOwO.\n"
        f"**{prefix}banbypass** - Prevents banning by taking breaks.\n"
        f"**{prefix}stats** - Shows command usage statistics.\n"
        "Example: the bot takes breaks (5 min, 10 min, 15 min, etc.)\n"
        "Made by Vicky | Support: https://discord.gg/Vd48FAZCGV"
    )

@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO is now **enabled** with smart features!')
    global dmcs, last_pray_time
    dmcs = True
    cycle_count = 0
    
    while dmcs:
        async with ctx.typing():
            # Randomize delays for human-like behavior
            delay1 = random.randint(4, 8)
            await asyncio.sleep(delay1)
            await ctx.send('owoh')
            cmd_stats['owoh'] += 1
            print(f"{Fore.GREEN}Successfully owoh")

            # Auto hunt
            delay2 = random.randint(2, 5)
            await asyncio.sleep(delay2)
            await ctx.send('owo hunt')
            cmd_stats['hunt'] += 1
            print(f"{Fore.GREEN}Successfully hunt")

            # Auto battle
            delay3 = random.randint(2, 5)
            await asyncio.sleep(delay3)
            await ctx.send('owo battle')
            cmd_stats['battle'] += 1
            print(f"{Fore.GREEN}Successfully battle")

            # Smart sell - ONLY animals without g,m,l,e letters
            delay4 = random.randint(8, 15)
            await asyncio.sleep(delay4)
            
            # Safe animals to sell (not containing g, m, l, e)
            safe_animals = [
                'cow', 'duck', 'cat', 'rat', 'bird', 'fish', 'ant', 'fox', 
                'bear', 'deer', 'boar', 'ox', 'yak', 'bison', 'shark', 'ray',
                'crab', 'squid', 'octopus', 'starfish', 'urchin', 'coral',
                'anemone', 'clam', 'oyster', 'scallop', 'conch', 'nautilus',
                'seahorse', 'pufferfish', 'tang', 'grouper', 'barracuda', 
                'tuna', 'salmon', 'trout', 'bass', 'pike', 'perch', 'carp', 
                'catfish', 'cod', 'haddock', 'flounder', 'sole', 'halibut', 
                'mackerel', 'sardine', 'anchovy', 'herring'
            ]
            
            # Sell safe animals one by one (NO sell all command)
            for animal in safe_animals:
                await ctx.send(f'owo sell {animal}')
                await asyncio.sleep(random.randint(1, 2))
                cmd_stats['sell'] += 1
                print(f"{Fore.GREEN}Smart sold: {animal}")

            # Flip
            await ctx.send('owo flip 500')
            cmd_stats['flip'] += 1
            print(f"{Fore.GREEN}Successfully owo flip 500")

            # Cash
            delay5 = random.randint(8, 15)
            await asyncio.sleep(delay5)
            await ctx.send('owo cash')
            cmd_stats['cash'] += 1
            print(f"{Fore.GREEN}Successfully cash")

            # Auto pray every 10 minutes
            now = time.time()
            if now - last_pray_time > 600:
                await ctx.send('owo pray')
                cmd_stats['pray'] += 1
                last_pray_time = now
                print(f"{Fore.GREEN}Successfully pray")

            # Every 3 cycles, check inventory for gems
            cycle_count += 1
            if cycle_count % 3 == 0:
                await ctx.send('owo inv')
                print(f"{Fore.GREEN}Checking inventory for gems...")
                await asyncio.sleep(5)  # Wait for OwO bot to reply

            # Final random sleep before next cycle
            await asyncio.sleep(random.randint(10, 18))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    # Only process messages from OwO Bot
    if str(message.author.id) not in ["1202830963034296360", "1202830963034296360"]:
        return
    
    # Auto-use gems when inventory is shown
    if hasattr(message, 'embeds') and message.embeds:
        embed = message.embeds[0]
        
        if embed.title and ("inventory" in embed.title.lower() or "backpack" in embed.title.lower()):
            await asyncio.sleep(2)  # Wait a bit before processing
            
            description = embed.description if embed.description else ''
            
            # Enhanced list of gems and items to use
            gem_patterns = [
                'hunting gem', 'luck gem', 'common gem', 'uncommon gem', 'rare gem', 
                'epic gem', 'legendary gem', 'mythical gem', 'special gem',
                'patreon gem', 'hidden gem', 'cowoncy gem', 'exp gem', 'daily gem',
                'huntbot', 'empowerment', 'efficiency', 'energize', 'enchant',
                'trap', 'magic', 'crate', 'lootbox', 'weapon', 'cookie', 'cake',
                'gem of luck', 'gem of hunting', 'gem of power'
            ]
            
            # Use each gem/item found
            for gem in gem_patterns:
                if gem.lower() in description.lower():
                    await asyncio.sleep(random.randint(1, 3))  # Random delay between uses
                    await message.channel.send(f'owo use {gem}')
                    print(f"{Fore.GREEN}Auto-used: {gem}")
    
    # Handle regular text messages for gem detection (fallback)
    elif "inventory" in message.content.lower() or "gem" in message.content.lower():
        content = message.content.lower()
        simple_gems = ['gem', 'huntbot', 'cookie', 'cake', 'crate']
        
        for gem in simple_gems:
            if gem in content:
                await asyncio.sleep(random.randint(2, 4))
                await message.channel.send(f'owo use {gem}')
                print(f"{Fore.GREEN}Fallback used: {gem}")

@bot.command()
async def stats(ctx):
    msg = (
        f"**AutoOwO Stats:**\n"
        f"owoh: {cmd_stats['owoh']}\n"
        f"hunt: {cmd_stats['hunt']}\n"
        f"battle: {cmd_stats['battle']}\n"
        f"sell: {cmd_stats['sell']}\n"
        f"flip: {cmd_stats['flip']}\n"
        f"cash: {cmd_stats['cash']}\n"
        f"pray: {cmd_stats['pray']}"
    )
    await ctx.send(msg)

@bot.command()
async def stopautoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO is now **disabled**!')
    global dmcs
    dmcs = False

@bot.command(pass_context=True)
async def banbypass(ctx):
    await ctx.message.delete()
    await ctx.send('banbypass is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(15)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(15)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(15)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(14)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(15)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(15)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(17)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(15)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(15)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(14)
            # REMOVED: await ctx.send('owo sell all')
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(300) 

@bot.event
async def on_ready():
    activity = discord.Game(name="DM for help", type=4)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

░█████╗░██╗░░░██╗████████╗░█████╗    ░░█████╗░░██╗░░░░░░░██╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗    ██╔══██╗░██║░░██╗░░██║██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║    ██║░░██║░╚██╗████╗██╔╝██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║    ██║░░██║░░████╔═████║░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝    ╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝    ░░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░


selfbot is ready!
''')

keep_alive()
try:
    bot.run(token)
except Exception as e:
    print(f"Error running bot: {e}")
    import traceback
    traceback.print_exc()
