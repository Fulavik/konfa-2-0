import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from asyncio import sleep
from datetime import timedelta, datetime, tzinfo, timezone

Bot = commands.Bot(command_prefix="//")

@Bot.command()
async def msg (ctx, arg):
    await ctx.send(arg)

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx,member:discord.Member,time:int,reason):
    channel = Bot.get_channel(771096859385004072)
    muterole = discord.utils.get(ctx.guild.roles,id=796680802175680555)
    timestamp = datetime.now()
    emb = discord.Embed(title='Информация о муте', color=0xff0000, timestamp=ctx.message.created_at)
    emb.add_field(name='Наказание выдал',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина наказания', value=reason,inline=False)
    emb.add_field(name='Длительность наказания (в секундах)',value=time,inline=False)
    await member.add_roles(muterole)
    await channel.send(embed = emb)
    await asyncio.sleep(time)
    await member.remove_roles(muterole)

@Bot.command()
@commands.has_role(714919688643150015)
async def sp(ctx,member:discord.Member = None,reason = None):
    channel = Bot.get_channel(788705539247964180)
    sprole = discord.utils.get(ctx.guild.roles,id=645362528641089566)
    admin = ctx.message.author
    timestamp = datetime.now()
    if not reason:
    	reason = 'Не указана'
    if not member:
    	await ctx.channel.send(f'Вы не указали пользователя.')
    	await asyncio.sleep(15)
    	await ctx.message.delete()
    await ctx.channel.send(f'{timestamp} {member.mention} был назначен на пост Spectator™, по запросу {admin.mention} Причина: {reason}')
    await member.add_roles(sprole)
    await member.send(f'{member.mention}, Ты принят на пост Модератора чата на сервере Конфа 2.0, Администратор принявший тебя: {admin.mention}, Причина: {reason}.')
   

Bot.run('ODQxMzk5ODUwMzE0MjM1OTY2.YJmMrA.83k07VC9w-DY8KFq70glhCIE5eY')