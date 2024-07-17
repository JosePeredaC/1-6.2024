import discord
from discord.ext import commands
import asyncio
# Configura los intents (esto es necesario para que el bot pueda recibir eventos como mensajes)
intents = discord.Intents.default()
intents.message_content = True  # Habilitar contenido de mensajes

# Crea una instancia de Bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Soy moises y me gusta euphoria')

@bot.command()
async def send_message(ctx, channel_id: int, *, message: str):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)
    else:
        await ctx.send(f'Channel with ID {channel_id} not found.')

# Función para enviar un mensaje desde la consola
async def send_message_from_console():
    while True:
        try:
            channel_id = int(input("Enter channel ID (0 to exit): "))
            if channel_id == 0:
                break
            
            message = input("Enter message to send: ")

            channel = bot.get_channel(channel_id)
            if channel:
                await channel.send(message)
            else:
                print(f'Channel with ID {channel_id} not found.')
        
        except ValueError:
            print("Invalid input. Please enter a valid channel ID.")

# Ejecutar el bot con tu token
async def main():
    await bot.start('')
    await send_message_from_console()

# Manejo de excepciones y finalización del bot
try:
    asyncio.run(main())
except KeyboardInterrupt:
    asyncio.run(bot.close())