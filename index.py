import discord
from discord.ext import commands
from colorama import Fore, Back, Style

client = commands.Bot(command_prefix=".", self_bot=True)

taevoz = client

@taevoz.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(1)
            print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Sleeping For {Fore.RED}1{Fore.RED}{Fore.RESET} Second")
            await user.send(message)
            print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Successfully {Fore.RED}Dmed{Fore.RED}{Fore.RESET} All")
        except:
            print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Couldn't Dmall {Fore.RED}1{Fore.RED}{Fore.RESET}")
            pass

taevoz.run("token", bot=False)
