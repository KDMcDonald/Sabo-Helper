import nextcord
from nextcord.ext import commands
from dotenv import dotenv_values

def main() -> None:
    bot : commands.bot = bot_init()
    bot.run(bot.secret_file['BOT_TOKEN'])
    print('Successful run')

def bot_init() -> commands.Bot:
    print('<< INITIALIZING BOT >>')
    bot = commands.Bot(command_prefix='.', intents=nextcord.Intents.all())
    bot.secret_file = dotenv_values('.env')

    bot.__version__ = '0.0.1'
    
    return bot

if __name__ == '__main__':
    main()