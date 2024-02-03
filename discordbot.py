import discord
from discord.ext import commands
from Frotz import Frotz

# dfrotz directory
# download dfrotz from : http://www.ifarchive.org/if-archive/infocom/interpreters/frotz/dfrotz.zip
# ref : http://www.ifarchive.org/indexes/if-archiveXinfocomXinterpretersXfrotz.html
dfrotz =  "dfrotz.exe" # replace this with the dfrotz exe location 

# games 
# Few are provided with the repo
# more can be found in : https://www.ifarchive.org/indexes/if-archiveXgamesXzcode.html
data = 'games/zork1.z5' # replace this with a game location

# Discord bot auth token
# https://discord.com/developers/docs/getting-started
TOKEN = 'YOUR DISCORD BOT TOKEN'


game = None
gameStart = False

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='start', help='Start game')
async def start(ctx):
    global gameStart
    global game
    gameStart = True
    game = Frotz(data, dfrotz)
    game_intro = game.get_intro()
    await ctx.send(game_intro)

@bot.command(name='stop', help='Stop game')
async def stop(ctx):
    global gameStart
    gameStart = False
    await ctx.send("Game stoped")

@bot.command(name='do', help='Do game action')
async def do(ctx):
    global gameStart
    global game
    if(gameStart):
        output = game.do_command(ctx.message.content.replace("!do", ""))
        await ctx.send(output)

bot.run(TOKEN)