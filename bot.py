import asyncio
import random
from discord.ext import commands
import discord
from discord import Member, embeds
from discord.ext.commands.bot import Bot
from discord.utils import get
import os
import time

Bot = commands.Bot(command_prefix='<')

@Bot.command(name="추방", pass_context=True)
@commands.has_any_role("관리자", "부관리자")
async def kick(ctx, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+", 넌 킥이다, 이 천하의 천치야! ")

@Bot.command(name="차단", pass_context=True)
@commands.has_any_role("관리자", "부관리자")
async def ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name)+", 넌 밴이다, 이 깡마른 깡통아! ")

@Bot.command(name="차단해제", pass_context=True)
@commands.has_any_role("관리자", "부관리자")
async def unban(ctx, *, user_name):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention}는/은 언밴되었다, 이 거대한 거위들아! ")

@Bot.command(name="뮤트", pass_context=True)
@commands.has_any_role("관리자", "부관리자", "VIP유저")
async def mute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.remove_roles(get(ctx.guild.roles, name='not Destroyed Program'))
    await member.add_roles(get(ctx.guild.roles, name="Destroyed Program"))
    await ctx.send(str(member)+", 넌 뮤트다 이 느끼한 느림보야! ")

@Bot.command(name="언뮤트", pass_context=True)
@commands.has_any_role("관리자", "부관리자", "VIP유저")
async def unmute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.remove_roles(get(ctx.guild.roles, name='Destroyed Program'))
    await member.add_roles(get(ctx.guild.roles, name="not Destroyed Program"))
    await ctx.send(str(member)+", 넌 언뮤트다, 이 배은망덕한 배신자야! ")

@Bot.command(name="청소", pass_context=True)
@commands.has_any_role("관리자", "컴퓨터")
async def clear(ctx, *, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(" 청소했다, 이 촌스러운 촌뜨기들아! ")
   
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{} 넌 권한이 없다, 이 비겁한 비렁뱅이야! ".format(ctx.message.author))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" 누구를 킥할 건지 쓰라고, 이 얼타는 얼간아! ")
    if isinstance(error, commands.BadArgument):
        await ctx.send(" 누구를 킥할 거냐고, 이 촌스러운 촌뜨기야! ")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("{} 넌 권한이 없다, 이 배은망덕한 배신자야! ".format(ctx.message.author))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" 누구를 밴할 건지 쓰라고, 이 멍청한 멍청아! ")
    if isinstance(error, commands.BadArgument):
        await ctx.send(" 누구를 밴할 거냐고, 이 굼뜬 굼벵아! ")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("{} 넌 권한이 없다, 이 느끼한 느림보야! ".format(ctx.message.author))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" 누구를 언밴할 건지 쓰라고, 이 풋풋한 풋내기야! ")
    if isinstance(error, commands.BadArgument):
        await ctx.send(" 누구를 언밴할 거냐고, 이 쓸모없는 쓰레기야! ")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("{} 넌 권한이 없다, 이 쓸모없는 쓰레기야! ".format(ctx.message.author))

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("{} 넌 권한이 없다, 이 느끼한 느림보야! ".format(ctx.message.author))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" 누구를 뮤트할 건지 쓰라고, 이 풋풋한 풋내기야! ")
    if isinstance(error, commands.BadArgument):
        await ctx.send(" 누구를 뮤트할 거냐고, 이 멍청한 멍청아! ")

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("{} 넌 권한이 없다, 이 느끼한 느림보야! ".format(ctx.message.author))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" 누구를 언뮤트할 건지 쓰라고, 이 고환 없는 고자야! ")
    if isinstance(error, commands.BadArgument):
        await ctx.send(" 누구를 언뮤트할 거냐고, 이 거대한 거위야! ")

Bot.run(os.environ['token'])
