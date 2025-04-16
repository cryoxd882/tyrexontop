import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

responses = {
    "payment": ("💳 Payment Methods", "We accept..."),
    "received": ("✅ Payment Received", "Thank you! Your payment has been received."),
    "done": ("🎉 Done!", "Your order is complete. Enjoy!")
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    content = message.content.lower()
    for key, (title, description) in responses.items():
        if key in content:
            embed = discord.Embed(title=title, description=description, color=discord.Color.blue())
            embed.set_footer(text="Tyrexᴳᴳ | CRYOxD")

            await message.channel.send(embed=embed)
            break

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
