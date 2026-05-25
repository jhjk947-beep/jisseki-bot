import discord
from discord.ext import commands
from discord.ui import View, Modal, TextInput
from datetime import datetime
import os

TOKEN = os.getenv("TOKEN")

RESULT_CHANNEL = "『📝』実績"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


class ReviewModal(Modal, title="購入実績を書く"):

    商品名 = TextInput(label="商品名", placeholder="例: Nitro")
    購入数量 = TextInput(label="購入数量", placeholder="例: 3")
    感想 = TextInput(
        label="感想",
        placeholder="取引の感想を書いてください",
        style=discord.TextStyle.paragraph
    )

    async def on_submit(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="📈 購入実績",
            description="```ご購入ありがとうございました```",
            color=0x5865F2
        )

        embed.add_field(name="📦 商品名", value=self.商品名, inline=False)
        embed.add_field(name="🛒 購入数量", value=f"{self.購入数量}件", inline=False)
        embed.add_field(name="💬 感想", value=f"```{self.感想}```", inline=False)
        embed.add_field(
            name="🕒 日時",
            value=datetime.now().strftime("%Y-%m-%d %H:%M"),
            inline=False
        )

        embed.set_footer(text=f"投稿者: {interaction.user}")

        result_channel = discord.utils.get(
            interaction.guild.text_channels,
            name=RESULT_CHANNEL
        )

        if result_channel:
            await result_channel.send(embed=embed)

        await interaction.response.send_message(
            "実績を投稿しました！",
            ephemeral=True
        )


class ReviewView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="実績を書く",
        style=discord.ButtonStyle.green,
        emoji="📝",
        custom_id="review_button"
    )
    async def review_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ReviewModal())


@bot.event
async def on_ready():
    bot.add_view(ReviewView())
    print(f"{bot.user} 起動完了")


@bot.command()
async def 設置(ctx):
    embed = discord.Embed(
        title="📈 実績記入",
        description="下のボタンを押して実績を書いてください",
        color=0x5865F2
    )

    await ctx.send(embed=embed, view=ReviewView())


bot.run(TOKEN)
