

@taevoz.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(1)
            print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Sleeping For {Fore.RED}1{Fore.RED}{Fore.RESET} Second")
            await user.send(message)
        except:
            pass
