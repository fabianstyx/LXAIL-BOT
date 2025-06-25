#nuevo
import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot connected successfully as {bot.user}")
    print(f"📊 Connected to {len(bot.guilds)} servers")

    activity = discord.Game(name="!updateLXAIL - LXAIL Updates")
    await bot.change_presence(activity=activity)

    # 🔁 Start the monitor
    bot.loop.create_task(monitor_pending_updates())


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Command not found. Use `!help` to see available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Missing required arguments. Use `!help updateLXAIL` for usage information.")
    else:
        await ctx.send(f"❌ An error occurred: {str(error)}")
        print(f"Command error: {error}")


@bot.command(name="updateLXAIL", help="Announces a new LXAIL update with changelog")
async def update_lxail(ctx, version: str = None):
    if version is None:
        await ctx.send("❌ Please provide a version number. Usage: `!updateLXAIL <version>`")
        return

    try:
        with open("changelog.txt", "r", encoding="utf-8") as f:
            changelog_content = f.read().strip()

        if not changelog_content:
            await ctx.send("❌ Changelog file is empty.")
            return

        embed = discord.Embed(
            title=f"📢 LXAIL Update - Version {version}",
            description="A new version of LXAIL has been released!",
            color=0x00ff00
        )

        if len(changelog_content) <= 1024:
            embed.add_field(name="📝 Changelog", value=f"```\n{changelog_content}\n```", inline=False)
        else:
            embed.add_field(name="📝 Changelog", value=f"```\n{changelog_content[:1000]}...\n```", inline=False)
            embed.add_field(name="📄 Full Changelog", value="See complete changelog in the following message.", inline=False)

        embed.set_footer(text=f"Update announced by {ctx.author.display_name}")
        embed.timestamp = ctx.message.created_at

        await ctx.send(embed=embed)

        if len(changelog_content) > 1024:
            chunks = [changelog_content[i:i + 1900] for i in range(0, len(changelog_content), 1900)]
            for i, chunk in enumerate(chunks):
                await ctx.send(f"```\n{chunk}\n```")

        print(f"✅ Update announcement sent for version {version} by {ctx.author}")

    except FileNotFoundError:
        await ctx.send("❌ 'changelog.txt' not found.")
        print("❌ changelog.txt not found")
    except Exception as e:
        await ctx.send(f"❌ Unexpected error: {str(e)}")
        print(f"❌ Unexpected error: {e}")


@bot.command(name="help_lxail", help="Shows help information for LXAIL bot commands")
async def help_lxail(ctx):
    embed = discord.Embed(
        title="🤖 LXAIL Update Bot - Help",
        description="Bot for announcing LXAIL software updates",
        color=0x0099ff)

    embed.add_field(name="!updateLXAIL <version>",
                    value="Announces a new LXAIL update with changelog info.",
                    inline=False)

    embed.add_field(name="!help_lxail", value="Shows this help message", inline=False)
    embed.add_field(name="📝 Setup",
                    value="Make sure `changelog.txt` and `pending_update.txt` exist in the bot folder.",
                    inline=False)
    embed.set_footer(text="LXAIL Update Bot")

    await ctx.send(embed=embed)


@bot.command(name="status", help="Shows bot status and information")
async def status(ctx):
    embed = discord.Embed(title="🤖 Bot Status", color=0x00ff00)
    embed.add_field(name="🔗 Connected", value="✅ Yes", inline=True)
    embed.add_field(name="📊 Servers", value=str(len(bot.guilds)), inline=True)
    embed.add_field(name="👥 Users", value=str(len(bot.users)), inline=True)

    try:
        with open("changelog.txt", "r") as f:
            content = f.read().strip()
        changelog_status = "✅ Available" if content else "⚠️ Empty"
    except FileNotFoundError:
        changelog_status = "❌ Not Found"
    except Exception:
        changelog_status = "❌ Error"

    embed.add_field(name="📝 Changelog", value=changelog_status, inline=True)
    await ctx.send(embed=embed)


async def monitor_pending_updates():
    await bot.wait_until_ready()
    channel_id = 1386976099975692308  # ✅ TU CANAL AQUÍ
    while not bot.is_closed():
        try:
            channel = bot.get_channel(channel_id)
            if not channel:
                await asyncio.sleep(5)
                continue

            with open("pending_update.txt", "r") as f:
                state = f.read().strip()

            if state != "OFF":
                version = state
                with open("changelog.txt", "r", encoding="utf-8") as f:
                    changelog = f.read().strip()

                embed = discord.Embed(
                    title=f"📢 LXAIL Update - Version {version}",
                    description="A new version of LXAIL has been released!",
                    color=0x00ff00
                )
                embed.add_field(name="📝 Changelog", value=f"```{changelog[:1000]}```", inline=False)
                embed.set_footer(text="LXAIL Helper (Auto)")
                await channel.send(embed=embed)

                with open("pending_update.txt", "w") as f:
                    f.write("OFF")

                print(f"✅ LXAIL HELPER sent update v{version}")

        except Exception as e:
            print(f"❌ Error in update monitor: {e}")

        await asyncio.sleep(10)


def main():
    if not TOKEN or TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Error: DISCORD_TOKEN not set in environment")
        return

    try:
        print("🚀 Starting LXAIL Update Bot...")
        bot.run(TOKEN)
    except discord.LoginFailure:
        print("❌ Invalid token")
    except discord.HTTPException as e:
        print(f"❌ HTTP Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
