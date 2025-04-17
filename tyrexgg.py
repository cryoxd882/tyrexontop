import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Define auto-responses
responses = {
    "hello": ("Hello!", "Hey there! How can I help you?"),
    "bye": ("Goodbye!", "See you soon!"),
    "how are you": ("I'm a bot!", "I'm just a bot, but I'm doing great!"),
    "payment": ("Payment Information",
        "**Bkash<:bkash:1347336576836833391>  | Nagad <:nagad:1347336634370097232> Same .**\n"
        "> **Number  **<:arrow_blue_4:1277679625006223472> 01933704619\n\n"
        "***Only accept Send Money.*** <:Money:1347336870027202742>\n\n"
        "**After Send Money Give a Screenshot of your transaction or last 4 digit of your Number.**\n\n"
        "You have to give extra 10tk for Nagad Only. <:wwdinosaur:1230981560996466781>"),
    "received": ("Payment Received",
        "**We have received your payment <:Money:1347336870027202742>**\n"
        "> Your order has been confirmed.<:right:1347354434069598250>\n\n"
        "<:time:1347355165082128446> **Your Order Complete Duration** <:arrow_blue_4:1277679625006223472> 5 - 360 Mins\n"
        "> Please Wait Till Your Order is Complete.\n\n"
        "**Thanks For Choosing Tyrexᴳᴳ**<:wwdinosaur:1230981560996466781>\n\n"
        "> **Be Patient**<a:patientwait:1347356364934086726>"),
    "done": ("Order Delivered",
        "**Hey <a:heart1:1347535693559103518>, Your Product is Successfully Delivered.**\n\n"
        "Kindly Give a [Review Here](https://discord.com/channels/1230520571754844331/1230520572874723470) ..!\n"
        "> Don't forget to add +rep at the beginning.\n\n"
        "<:alert:1347346058409410752> **Remember No [Review](https://discord.com/channels/1230520571754844331/1230520572874723470) = No Warranty..!**\n\n"
        "**See Yaa! <:wwdinosaur:1230981560996466781>**"),
    "vp": ("Valorant Point Topup Rules",
        "<a:vaorant:1347536941704413205> **Valorant Point Topup Rules :**\n\n"
        "**You have to give your in-game & hashtag (#tag) accurately. It's sensitive.**\n"
        "> Example : xyz#999\n\n"
        "# **Bangladesh (BGD) VP purchase Rule:**\n\n"
        "> We'll provide you a redeem code to claim VP. <:wwdinosaur:1230981560996466781>"),
    "nitro": ("<a:nitro:1347539220238958675> **NITRO BOOST PREMIUM!**",
        "**GIFT LINK  ** \n"
        "**<:bs_dot:1261240181265137686> 1 Month <a:ch_arrow3:1260577273204051969> 600 ৳**\n"
        "**<:bs_dot:1261240181265137686> 1 Year     <a:ch_arrow3:1260577273204051969>  6000 ৳**\n\n"
        "**Promo**\n"
        "**<:bs_dot:1261240181265137686>3 Month Promo <a:ch_arrow3:1260577273204051969> 300 taka **\n"
        "> **(Id age must be 1 month old and never had nitro before)**\n"
        "> **(Login Credential Needed)**\n\n"
        "**<:wwdinosaur:1230981560996466781> Must Check Out <#1230520572266418286> Before Buy Anything!!**\n\n"
        "**<a:note:1193526991559872595> Price Can Be Changed Anytime!**\n\n"
        "**Create A Ticket To <#1230520573180903509>!!**")
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself
    
    content = message.content.lower()
    for key, (title, description) in responses.items():
        if key in content:
            embed = discord.Embed(title=title, description=description, color=discord.Color.blue())
            embed.set_footer(text="Tyrexᴳᴳ | CRYOxDpython bot.py")
            
            # Add image and thumbnail only for payment response
            if key == "payment":
                embed.set_image(url="https://media.discordapp.net/attachments/1249673368907681897/1347330899494309888/White_Pink_Illustrative_Cute_QR_Code_Flayer.png?ex=67cc17ee&is=67cac66e&hm=75ee811aa251dec1c52cc30bc64993df405cc75f84488e6e9d9604790dae247b&=&format=webp&quality=lossless&width=679&height=960")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1249673368907681897/1249675076756967444/Untitled_design_10.png?ex=67cb765c&is=67ca24dc&hm=53f8adaea07ae2931c0d03767cd1c89f4f01466d8d71aee9f8cde3b6dc025d28&=&format=webp&quality=lossless")
            
            # Add image and thumbnail only for received response
            if key == "received":
                embed.set_image(url="https://media.discordapp.net/attachments/1249673368907681897/1347352939227775006/rsz_black_and_green_bold_gradient_brutalist_graphic_discord_profile_banner_4.png?ex=67cb83b5&is=67ca3235&hm=1276c4365fae6fa986e872baebf0263cc97fdbc0d5e3f9e938affae59930c3ef&=&format=webp&quality=lossless")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1249673368907681897/1249675076756967444/Untitled_design_10.png?ex=67cb765c&is=67ca24dc&hm=53f8adaea07ae2931c0d03767cd1c89f4f01466d8d71aee9f8cde3b6dc025d28&=&format=webp&quality=lossless")
            
            # Add image only for done response
            if key == "done":
                embed.set_image(url="https://media.discordapp.net/attachments/1249673368907681897/1347344782485094420/Black_and_Green_Bold_Gradient_Brutalist_Graphic_Discord_Profile_Banner_3.png?ex=67cc24dc&is=67cad35c&hm=cdd0203b860499d689353dbabcd1151b1a92952ec358f4cea5b2e20f253cef19&=&format=webp&quality=lossless&width=1872&height=749")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1249673368907681897/1249675076756967444/Untitled_design_10.png?ex=67cb765c&is=67ca24dc&hm=53f8adaea07ae2931c0d03767cd1c89f4f01466d8d71aee9f8cde3b6dc025d28&=&format=webp&quality=lossless")
            
            await message.channel.send(embed=embed)
            break  # Prevent multiple responses

    await bot.process_commands(message)  # Ensure commands still work can you copy it

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
