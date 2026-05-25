import discord
from discord.ext import commands
from datetime import datetime
import os

TOKEN = os.getenv("TOKEN")
ALLOWED_CHANNEL = "実績"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

jisseki_no = 1

@bot.event
async def on_ready():
    print(f"{bot.user} が起動しました")

@bot.command()
async def 実績(ctx, 商品名, 数量: int):
    global jisseki_no

    if ctx.channel.name != ALLOWED_CHANNEL:
        return

    embed = discord.Embed(
        title=f"📈 販売実績 #{jisseki_no}",
        color=0x00ff00
    )

    embed.add_field(name="商品名", value=商品名, inline=False)
    embed.add_field(name="購入数", value=f"{数量}件", inline=False)
    embed.add_field(
        name="日時",
        value=datetime.now().strftime("%Y-%m-%d %H:%M"),
        inline=False
    )

    await ctx.send(embed=embed)
    await ctx.message.delete()

    jisseki_no += 1

bot.run(TOKEN)
