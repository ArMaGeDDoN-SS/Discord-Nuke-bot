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


class Developer(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['black_add', 'black_append', 'bl_append'], pass_context=True)
    async def bl_add(self, ctx, id_user):

        if ctx.author.id in developer_list:

            with open("json/black_list.json", 'r', encoding="utf-8") as bl:
                black_l = json.load(bl)

            if id_user != None:

                if int(id_user) in black_l:

                    embed = discord.Embed(
                        title = "❗ | Ошибка! Пользователь с указанным ID уже занесён в чёрный список!",
                        description = f"**Анализ чёрного списка показал, что пользователь с указанным вами ID уже занесён в чёрный список.**\n\n**🆔・User ID: `{id_user}`**",
                        color = 0xFF0000
                    )
                    embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                    await ctx.send(embed=embed)

                else:

                    black_l.append(int(id_user))
                    with open('json/black_list.json', 'w') as bl:
                        json.dump(black_l, bl)

                    embed = discord.Embed(
                        title = f"✅ | The participant has been added to the blacklist.",
                        description = f"**The participant with the specified ID was successfully added to the blacklist, from that moment he is denied access to all crash bot commands. If the person you added was blacklisted by mistake, remove him from the list using the command `!bl_delete`.**\n\n**🆔・User ID: `{id_user}`**",
                        color = 0x4CFF00
                    )
                    embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046810941695725588/image.png", text="Blood Group - Official")
                    await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    title = "❗ | Ошибка! Вы не указали ID нужного пользователя!",
                    description = f"**Во время написания команды вы не указали ID пользователя, которого хотели добавить в чёрный список. Пропишите команду снова, предварительно указав ID участника.**",
                    color = 0xFF0000
                )
                embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                await ctx.send(embed=embed)

        else:

            embed = discord.Embed(
                title = "🔒 | Вам запрещено использовать использовать служебные команды!",
                description = f"**Доброго времени суток, <@{ctx.author.id}>, вам запрещено использовать служебную команду `!bl_add`, так как вы не являетесь разработчиком данного бота.**",
                color = 0xFF0000
            )
            embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
            await ctx.send(embed=embed)


    @commands.command(aliases=['bl_remove', 'black_remove', 'black_delete'], pass_context=True)
    async def bl_delete(self, ctx, id_user=None):

        if ctx.author.id in developer_list:

            with open("json/black_list.json", 'r', encoding="utf-8") as bl:
                black_l = json.load(bl)

            if id_user != None:

                if int(id_user) in black_l:

                    black_l.remove(int(id_user))
                    with open('json/black_list.json', 'w') as bl:
                        json.dump(black_l, bl)

                    embed = discord.Embed(
                        title = f"✅ | Участник был удалён.",
                        description = f"**Упомянутый вами участник был успешно удалён из чёрного списка, ему возвращён доступ ко всем командам бота. В случае, если был удалён не тот участник - верните недавно удалённого в чёрный список при помощи команды `!bl_add`.**\n\n**🆔・User ID: `{id_user}`**",
                        color = 0x4CFF00
                    )
                    embed.set_footer(icon_url=f"https://media.discordapp.net/attachments/1045645133003104270/1046810941695725588/image.png", text="Blood Group - Official")
                    await ctx.author.send(embed=embed)

                else:
                    embed = discord.Embed(
                        title = "❗ | Ошибка! Указанного ID нет в чёрном списке.",
                        description = f"**Анализ чёрного списка показал, что пользователя с указанным вами ID - в чёрном списке нет.**\n\n**🆔・User ID: `{id_user}`**",
                        color = 0xFF0000
                    )
                    embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                    await ctx.author.send(embed=embed)

            else:
                embed = discord.Embed(
                    title = "❗ | Ошибка! Вы не указали ID нужного пользователя!",
                    description = f"**Во время написания команды вы не указали ID пользователя, которого хотели удалить из чёрного списка. Пропишите команду снова, предварительно указав ID участника.**",
                    color = 0xFF0000
                )
                embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                await ctx.author.send(embed=embed)

        else:

            embed = discord.Embed(
                title = "🔒 | Вам запрещено использовать использовать служебные команды!",
                description = f"**Доброго времени суток, <@{ctx.author.id}>, вам запрещено использовать служебную команду `!bl_delete`, так как вы не являетесь разработчиком данного бота.**",
                color = 0xFF0000
            )
            embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
            await ctx.author.send(embed=embed)



    @commands.command(pass_context=True)
    async def wl_add(self, ctx, id_guild=None):

        if ctx.author.id in deceloper_list:

            with open("json/white_list.json", 'r', encoding="utf-8") as wl:
                white_list = json.load(wl)

            if id_guild is None:

                embed = discord.Embed(
                    title = "❗ | Ошибка! Вы не указали ID нужного сервера!",
                    description = "**Чтобы добавить какой-либо сервер в белый список - укажите его `ID` во время вызова команды `!wl_add`.**",
                    color = 0xFF0000
                )
                embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                await ctx.author.send(embed=embed)

            else:

                if id_guild in white_list:

                    embed = discord.Embed(
                        title = "❗ | Ошибка! Сервер с указанным ID уже занесён в белый список!",
                        description = f"**Анализ белого списка показал, что сервер с указанным вами ID уже занесён в белый список.**\n\n**🆔・Server ID: `{id_guild}`**",
                        color = 0xFF0000
                    )
                    embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                    await ctx.send(embed=embed)

                else:

                    white_list.append(int(id_user))
                    with open('json/white_list.json', 'w') as wl:
                        json.dump(white_list, wl)

                    embed = discord.Embed(
                        title = "✅ | Сервер был успешно добавлен в белый список!",
                        description = f"**Указанный вами сервер был добавлен в белый список. В случае, если сервер, который вы добавили, был добавлен ошибочно, то удалите его из белого списка при помощи команды `!wl_delete`.**\n\n**🆔・Server: `{id_guild}`.**",
                        color = 0xFF0000
                    )
                    embed.set_footer(icon_url=f"https://media.discordapp.net/attachments/1045645133003104270/1046810941695725588/image.png", text="Blood Group - Official")
                    await ctx.author.send(embed=embed)

        else:

            embed = discord.Embed(
                title = "🔒 | Вам запрещено использовать использовать служебные команды!",
                description = f"**Доброго времени суток, <@{ctx.author.id}>, вам запрещено использовать служебную команду `!wl_add`, так как вы не являетесь разработчиком данного бота.**",
                color = 0xFF0000
            )
            embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
            await ctx.author.send(embed=embed)


    @commands.command(pass_context=True)
    async def wl_delete(self, ctx, id_guild=None):

        if ctx.author.id in developer_list:

            with open("json/white_list.json", 'r', encoding="utf-8") as wl:
                white_list = json.load(bl)

            if id_guild != None:

                if int(id_user) in black_l:

                    white_list.remove(int(id_user))
                    with open('json/white_list.json', 'w') as bl:
                        json.dump(black_l, bl)

                    embed = discord.Embed(
                        title = f"✅ | Сервер был удалён из белого списока.",
                        description = f"**Указанный вами сервер был удалён из белого списка, с этого момента бот может спокойно уничтожить этот сервер.**\n\n**🆔・Server ID: `{id_guild}`**",
                        color = 0x4CFF00
                    )
                    embed.set_footer(icon_url=f"https://media.discordapp.net/attachments/1045645133003104270/1046810941695725588/image.png", text="Blood Group - Official")
                    await ctx.author.send(embed=embed)

                else:
                    embed = discord.Embed(
                        title = "❗ | Ошибка! Указанного ID нет в белом списке.",
                        description = f"**Анализ белого списка показал, что сервера с указанным вами ID - в белом списке нет.**\n\n**🆔・User ID: `{id_guild}`**",
                        color = 0xFF0000
                    )
                    embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                    await ctx.author.send(embed=embed)

            else:
                embed = discord.Embed(
                    title = "❗ | Ошибка! Вы не указали ID нужного пользователя!",
                    description = f"**Во время написания команды вы не указали ID пользователя, которого хотели удалить из белого списка. Пропишите команду снова, предварительно указав ID нужного вам сервера.**",
                    color = 0xFF0000
                )
                embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
                await ctx.author.send(embed=embed)

        else:

            embed = discord.Embed(
                title = "🔒 | Вам запрещено использовать использовать служебные команды!",
                description = f"**Доброго времени суток, <@{ctx.author.id}>, вам запрещено использовать служебную команду `!wl_delete`, так как вы не являетесь разработчиком данного бота.**",
                color = 0xFF0000
            )
            embed.set_footer(icon_url="https://media.discordapp.net/attachments/1045645133003104270/1046444713546362921/image.png", text="Blood Group - Official")
            await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(Developer(client))