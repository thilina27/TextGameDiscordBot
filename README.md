## Discord bot to play text based game (ex : Zork) in discord. 

##### NOTE : Tested only on windows
### How to run 

#### Prerequisite 
* [Python 3.*](https://www.python.org/downloads/) 
* [Discordpy](https://discordpy.readthedocs.io/en/stable/)
* Dumb Frotz ([Windows download](http://www.ifarchive.org/if-archive/infocom/interpreters/frotz/dfrotz.zip))

### Step 1
1. Unzip Dumb Frotz.
2. Download source code of bot from github.
3. Create and Discord bot ([How to make a discord bot](https://discord.com/developers/docs/getting-started)).
4. Copy created discord bot token.

### Step 2
1. Open `discordbot.py`.
2. Reaplace exe path in [`dfrotz =  "dfrotz.exe"`](https://github.com/thilina27/TextGameDiscordBot/blob/3c69791f82ffc416bad56a3e5be0abda524abd04/discordbot.py#L8), with location of your Dumb Frotz exe.
3. Repalce [`TOKEN = 'YOUR DISCORD BOT TOKEN'`](https://github.com/thilina27/TextGameDiscordBot/blob/3c69791f82ffc416bad56a3e5be0abda524abd04/discordbot.py#L17C1-L17C33) with your bot auth token.

### Step 3 
1. Add bot to your discord server.
2. Run `discordbot.py`.
3. PLAY 😄

#### Sone games are provided in game directory in the repo. You can change the game on [`data = 'games/zork1.z5'`](https://github.com/thilina27/TextGameDiscordBot/blob/0a7c3ad1883abd93df99c102baad792c79f1d848/discordbot.py#L13)
#### More can be found in : https://www.ifarchive.org/indexes/if-archiveXgamesXzcode.html

### Available commands 
#### !start - Start game 
#### !stop  - Stop game
#### !do <action> - Do provided action in game

![Sample](https://github.com/thilina27/TextGameDiscordBot/blob/main/sample.png)
