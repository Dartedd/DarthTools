import discord
from discord.ext import commands
import asyncio

# Define the bot command
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True  # Required to access member information

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('Use ?kill [channels/role name] to delete all channels, roles and create new ones.')
    print('Use ?banall to ban every member in the server.')
    print('Use ?nickname all [nickname] to change everyone\'s nickname.     NEED THE RIGHT PERMISSIONS THO!')
    print('Use ?spam [message] [count] to spam every text channel with the specified message.')


@bot.command()
@commands.has_permissions(administrator=True)
async def kill(ctx, *, name: str = None):
    guild = ctx.guild

    # Delete all channels
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Deleted channel {channel.name}')
        except discord.Forbidden:
            print(f'No permission to delete {channel.name}')
        except discord.HTTPException as e:
            print(f'Failed to delete {channel.name}: {e}')

    # Delete all roles
    for role in guild.roles:
        if role.name != "@everyone":  # Don't delete the @everyone role
            try:
                await role.delete()
                print(f'Deleted role {role.name}')
            except discord.Forbidden:
                print(f'No permission to delete {role.name}')
            except discord.HTTPException as e:
                print(f'Failed to delete {role.name}: {e}')

    # Create new channels and roles
    if name:
        for i in range(50):
            try:
                await guild.create_text_channel(f'{name} Text {i + 1}')
                await guild.create_voice_channel(f'{name} Voice {i + 1}')
                print(f'Created {name} Text {i + 1} and {name} Voice {i + 1}')
            except discord.Forbidden:
                print(f'No permission to create channels.')
            except discord.HTTPException as e:
                print(f'Failed to create channels: {e}')

        for i in range(100):
            try:
                await guild.create_role(name=f'{name} Role {i + 1}')
                print(f'Created role {name} Role {i + 1}')
            except discord.Forbidden:
                print(f'No permission to create roles.')
            except discord.HTTPException as e:
                print(f'Failed to create roles: {e}')

        await ctx.send(f'50 text channels, 50 voice channels, and 100 roles named "{name}" created!')


@bot.command()
@commands.has_permissions(administrator=True)
async def banall(ctx):
    guild = ctx.guild

    # Ban all members except the bot itself and the command sender
    for member in guild.members:
        if member.id != bot.user.id and member.id != ctx.author.id:
            try:
                await member.ban(reason="Banned by bot command")
                print(f'Banned {member.name}')
            except discord.Forbidden:
                print(f'No permission to ban {member.name}')
            except discord.HTTPException as e:
                print(f'Failed to ban {member.name}: {e}')

    await ctx.send('All members have been banned (except bot and command sender)!')


@bot.command()
@commands.has_permissions(administrator=True)
async def nickname(ctx, *, nickname: str = None):
    guild = ctx.guild

    if not nickname:
        await ctx.send("Please provide a nickname to set for all members.")
        return

    # Change the nickname of all members except the bot itself
    for member in guild.members:
        if member.id != bot.user.id:
            try:
                await member.edit(nick=nickname)
                print(f'Changed nickname of {member.name} to {nickname}')
            except discord.Forbidden:
                print(f'No permission to change nickname of {member.name}')
            except discord.HTTPException as e:
                print(f'Failed to change nickname of {member.name}: {e}')

    await ctx.send(f'All members have been given the nickname "{nickname}"!')


@bot.command()
@commands.has_permissions(administrator=True)
async def spam(ctx, *, message_info: str):
    guild = ctx.guild
    parts = message_info.split(' ', 1)

    if len(parts) != 2:
        await ctx.send("Please provide a message and the number of times to spam.")
        return

    message, count_str = parts
    try:
        count = int(count_str)
    except ValueError:
        await ctx.send("Invalid number of messages. Please enter a numeric value.")
        return

    if count <= 0:
        await ctx.send("The number of messages must be greater than 0.")
        return

    # Spam every text channel in the guild
    for channel in guild.text_channels:
        for i in range(count):
            try:
                await channel.send(message)
                print(f'Sent message in channel {channel.name} ({i + 1}/{count})')
            except discord.Forbidden:
                print(f'No permission to send messages in {channel.name}')
            except discord.HTTPException as e:
                print(f'Failed to send message in {channel.name}: {e}')
            await asyncio.sleep(1)  # Small delay to avoid rate limits

    await ctx.send(f'Sent "{message}" {count} times in all text channels!')


def run_bot(token):
    bot.run(token)


def main():
    token = input("Enter your Discord bot token: ").strip()
    if not token:
        print("Error: Bot token cannot be empty.")
        return

    print("Running bot...")
    run_bot(token)


if __name__ == "__main__":
    main()
