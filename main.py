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
import re

#-----SETUP-----#
prefix = ">"

# Use the .env feature to hide your token
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
        f"**{prefix}autoOwO** - owoh, smart sell (c/r/u only), owo flip 500 and owo cash with auto gem usage.\n"
        f"**{prefix}stopautoOwO** - stops autoOwO.\n"
        f"**{prefix}banbypass** - Prevents banning by taking breaks.\n"
        f"**{prefix}stats** - Shows command usage statistics.\n"
        "**SAFE TIMING** - Uses owo sell c/r/u commands!\n"
        "Made by Vicky | Support: https://discord.gg/Vd48FAZCGV"
    )

@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO is now **enabled** with SAFE c/r/u selling and numbered gem detection!')
    global dmcs, last_pray_time
    dmcs = True
    cycle_count = 0
    
    while dmcs:
        async with ctx.typing():
            # MUCH LONGER delays for human-like behavior and rate limit avoidance
            delay1 = random.randint(12, 20)
            await asyncio.sleep(delay1)
            await ctx.send('owoh')
            cmd_stats['owoh'] += 1
            print(f"{Fore.GREEN}Successfully owoh")

            # Auto hunt with longer delay
            delay2 = random.randint(10, 15)
            await asyncio.sleep(delay2)
            await ctx.send('owo hunt')
            cmd_stats['hunt'] += 1
            print(f"{Fore.GREEN}Successfully hunt")

            # Auto battle with longer delay
            delay3 = random.randint(10, 15)
            await asyncio.sleep(delay3)
            await ctx.send('owo battle')
            cmd_stats['battle'] += 1
            print(f"{Fore.GREEN}Successfully battle")

            # LONGER break before selling
            delay4 = random.randint(25, 40)
            await asyncio.sleep(delay4)
            
            # SAFE selling using c/r/u categories instead of individual animals
            sell_categories = ['c', 'r', 'u']  # common, rare, uncommon
            
            for category in sell_categories:
                await ctx.send(f'owo sell {category}')
                await asyncio.sleep(random.randint(8, 15))  # Safe delays between category sells
                cmd_stats['sell'] += 1
                print(f"{Fore.GREEN}Smart sold category: {category}")

            # LONGER break before flip
            await asyncio.sleep(random.randint(15, 25))
            await ctx.send('owo flip 500')
            cmd_stats['flip'] += 1
            print(f"{Fore.GREEN}Successfully owo flip 500")

            # Cash with longer delay
            delay5 = random.randint(20, 30)
            await asyncio.sleep(delay5)
            await ctx.send('owo cash')
            cmd_stats['cash'] += 1
            print(f"{Fore.GREEN}Successfully cash")

            # Auto pray every 10 minutes
            now = time.time()
            if now - last_pray_time > 600:
                await asyncio.sleep(random.randint(5, 10))
                await ctx.send('owo pray')
                cmd_stats['pray'] += 1
                last_pray_time = now
                print(f"{Fore.GREEN}Successfully pray")

            # Check inventory less frequently (every 5 cycles)
            cycle_count += 1
            if cycle_count % 5 == 0:
                await asyncio.sleep(random.randint(10, 15))
                await ctx.send('owo inv')
                print(f"{Fore.GREEN}Checking inventory for gems (cycle {cycle_count})...")
                await asyncio.sleep(12)  # Wait longer for OwO bot to reply

            # Random extended breaks to simulate human behavior
            if random.randint(1, 10) <= 2:  # 20% chance
                extended_break = random.randint(60, 120)  # 1-2 minute break
                print(f"{Fore.YELLOW}Taking extended break ({extended_break}s) to avoid rate limits...")
                await asyncio.sleep(extended_break)

            # MUCH LONGER final cycle delay
            final_delay = random.randint(50, 80)
            print(f"{Fore.CYAN}Cycle {cycle_count} complete. Next cycle in {final_delay}s...")
            await asyncio.sleep(final_delay)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    # Only process messages from OwO Bot (updated IDs)
    if str(message.author.id) not in ["408785106942164992", "519287796549156864"]:
        return
    
    # Auto-use gems when inventory is shown
    if hasattr(message, 'embeds') and message.embeds:
        embed = message.embeds[0]
        
        if embed.title and ("inventory" in embed.title.lower() or "backpack" in embed.title.lower()):
            await asyncio.sleep(random.randint(3, 6))  # Longer wait before processing
            
            description = embed.description if embed.description else ''
            
            # Enhanced list of named gems and items to use
            gem_patterns = [
                'hunting gem', 'luck gem', 'common gem', 'uncommon gem', 'rare gem', 
                'epic gem', 'legendary gem', 'mythical gem', 'special gem',
                'patreon gem', 'hidden gem', 'cowoncy gem', 'exp gem', 'daily gem',
                'huntbot', 'empowerment', 'efficiency', 'energize', 'enchant',
                'trap', 'magic', 'crate', 'lootbox', 'weapon', 'cookie', 'cake'
            ]
            
            # Use named gems with SAFER delays
            for gem in gem_patterns:
                if gem.lower() in description.lower():
                    await asyncio.sleep(random.randint(5, 10))  # Much longer delays
                    await message.channel.send(f'owo use {gem}')
                    print(f"{Fore.GREEN}Auto-used named gem: {gem}")
            
            # Check for numbered gems (051-075) with SAFER delays
            numbered_gems = re.findall(r'(0[5-7][0-9])[\d⁰¹²³⁴⁵⁶⁷⁸⁹]*', description)
            
            for gem_number in numbered_gems:
                if 51 <= int(gem_number) <= 75:
                    await asyncio.sleep(random.randint(8, 15))  # Even longer delays for numbered gems
                    await message.channel.send(f'owo use {gem_number}')
                    print(f"{Fore.GREEN}Auto-used numbered gem: {gem_number}")
    
    # Handle regular text messages for gem detection (fallback)
    elif "inventory" in message.content.lower():
        content = message.content
        
        # Check for numbered gems in plain text with delays
        numbered_gems = re.findall(r'(0[5-7][0-9])', content)
        
        for gem_number in numbered_gems:
            if 51 <= int(gem_number) <= 75:
                await asyncio.sleep(random.randint(8, 15))
                await message.channel.send(f'owo use {gem_number}')
                print(f"{Fore.GREEN}Fallback used numbered gem: {gem_number}")

@bot.command()
async def stats(ctx):
    msg = (
        f"**AutoOwO Stats:**\n"
        f"owoh: {cmd_stats['owoh']}\n"
        f"hunt: {cmd_stats['hunt']}\n"
        f"battle: {cmd_stats['battle']}\n"
        f"sell (c/r/u): {cmd_stats['sell']}\n"
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
    await ctx.send('banbypass is now **enabled** with c/r/u selling!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            # SAFER banbypass with c/r/u selling
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(random.randint(20, 30))
            
            # Sell by categories instead of individual animals
            await ctx.send('owo sell c')
            print(f"{Fore.GREEN}successfully sell common")
            await asyncio.sleep(random.randint(8, 12))
            
            await ctx.send('owo sell r')
            print(f"{Fore.GREEN}successfully sell rare")
            await asyncio.sleep(random.randint(8, 12))
            
            await ctx.send('owo sell u')
            print(f"{Fore.GREEN}successfully sell uncommon")
            await asyncio.sleep(random.randint(8, 12))
            
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(random.randint(15, 20))
            
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(random.randint(20, 25))
            
            await ctx.send('owoh')
            print(f"{Fore.GREEN}successfully owoh")
            await asyncio.sleep(random.randint(20, 30))
            
            # Sell categories again
            await ctx.send('owo sell c')
            await asyncio.sleep(random.randint(8, 12))
            await ctx.send('owo sell r') 
            await asyncio.sleep(random.randint(8, 12))
            await ctx.send('owo sell u')
            await asyncio.sleep(random.randint(8, 12))
            
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}successfully owo flip 500")
            await asyncio.sleep(random.randint(15, 20))
            
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}successfully cash")
            await asyncio.sleep(random.randint(20, 25))
            
            # Extended break between cycles
            print(f"{Fore.YELLOW}Taking 10-minute break to avoid detection...")
            await asyncio.sleep(random.randint(600, 900))  # 10-15 minute breaks

@bot.event
async def on_ready():
    activity = discord.Game(name="Safe AutoOwO c/r/u v2.1", type=4)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝

{Fore.GREEN}
░█████╗░██╗░░░██╗████████╗░█████╗    ░░█████╗░░██╗░░░░░░░██╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗    ██╔══██╗░██║░░██╗░░██║██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║    ██║░░██║░╚██╗████╗██╔╝██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║    ██║░░██║░░████╔═████║░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝    ╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝    ░░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░

{Fore.CYAN}C/R/U SELLING VERSION - Category-Based Safe Selling!
{Fore.WHITE}selfbot is ready!
''')

keep_alive()
try:
    bot.run(token)
except Exception as e:
    print(f"Error running bot: {e}")
    import traceback
    traceback.print_exc()
