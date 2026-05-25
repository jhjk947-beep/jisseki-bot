discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
from datetime import datetime
import os

TOKEN = os.getenv("TOKEN")
ALLOWED_CHANNEL = "実績"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


class ReviewModal(Modal, title="購入実績を記入"):

    商品名 = TextInput(label="商品名", placeholder="例: Nitro")
    購入数量 = TextInput(label="購入数量", placeholder="例: 3")
    感想 = TextInput(
        label="ご感想",
        placeholder="取引の感想を書いてください",
        style=discord.TextStyle.paragraph
    )

    async def on_submit(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="✅ 取引完了",
            description="```ご購入ありがとうございました```",
            color=0x00ff88
        )

        embed.add_field(
            name="📦 商品情報",
            value=f"**商品名:** {self.商品名}",
            inline=False
        )

        embed.add_field(
            name="🛒 購入数量",
            value=f"**{self.購入数量}件**",
            inline=False
        )

        embed.add_field(
            name="💬 ご感想",
            value=f"```{self.感想}```",
            inline=False
        )

        embed.add_field(
            name="🕒 取引日時",
            value=datetime.now().strftime("%Y-%m-%d %H:%M"),
            inline=False
        )

        embed.add_field(
            name="💎 STATUS",
            value="```Trusted Seller```\n```取引完了```",
            inline=False
        )

        embed.set_footer(text=f"レビュー投稿者: {interaction.user}")

        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(
            "実績を投稿しました！",
            ephemeral=True
        )


class ReviewButton(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="実績を書く",
        style=discord.ButtonStyle.green,
        emoji="📝"
    )
    async def review_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(ReviewModal())


@bot.event
async def on_ready():
    @bot.event
async def on_ready():
    print(f"{bot.user} 起動完了")
    b
    print(f"{bot.user} 起動完了")


@bot.command()
async def 設置(ctx):
    if ctx.channel.name != ALLOWED_CHANNEL:
        return

    embed = discord.Embed(
        title="📈 購入実績投稿",
        description="下のボタンから購入実績を投稿してください",
        color=0x5865F2
    )

    await ctx.send(embed=embed, view=ReviewButton())


bot.run(TOKEN)

