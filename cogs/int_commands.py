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


class Int_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Creating the specified number of channels
    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def intchannels(self, ctx, m):

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

                if int(m) <= 100 and int(m) > 0:
                    for i in range(int(m)):
                        try:
                            await ctx.guild.create_text_channel(channels_name)
                        except:
                            try:
                                await ctx.guild.create_text_channel(channels_name)
                            except:
                                pass

                else:
                    embed = discord.Embed(
            	        title = "Error!",
            	        description = f"""
**<@{ctx.author.id}>, you have specified too many channels to create.
> The maximum number of channels that can be specified: `100`.
> The maximum number of channels that can be specified: `1`.**""",
            	        color = 0xFF0000
                    )
                    embed.set_footer(
                        icon_url = 'https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png',
                        text = 'Blood Group・Hydra Team'
                    )
                    await ctx.send(embed=embed)

            except Exception as e: print(e)


    # Creating the specified number of roles
    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def introles(self, ctx, m):

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

                if int(m) <= 100 and int(m) > 0:
                    for i in range(int(m)):
                        try:
                            await ctx.guild.create_role(name=roles_name)
                        except:
                            try:
                                await ctx.guild.create_role(name=roles_name)
                            except:
                                pass
                else:
                    embed = discord.Embed(
                        title = "Ошибка!",
                        description = f"""
**<@{ctx.author.id}>, you have specified too many roles to create.
> The maximum number of roles that can be specified: `100`.
> The minimum number of roles that can be specified: `1`.**""",
                        color = 0xFF0000
                    )
                    embed.set_footer(
                        icon_url = 'https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png',
                        text = 'Blood Group・Hydra Team'
                    )
                    await ctx.send(embed=embed)

            except Exception as e: print(e)


def setup(client):
    client.add_cog(Int_Commands(client))
