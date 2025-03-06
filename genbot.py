import discord
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up OpenAI
openai.api_key = OPENAI_API_KEY

# Initialize Discord bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Function to get OpenAI response
def ask_openai(prompt):    
        return "AI functionality under construction :P"

# Event when bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event to process messages
@client.event
async def on_message(message):

    print(f"Received message: {message.content} from {message.author}")  # Debugging line

    if message.author == client.user:
        return

    user_input = message.content

    # Check if the bot is mentioned
    if client.user in message.mentions:
        await message.channel.send("AI functionality under construction :P")
        return
    else:
        return

    # Simple safeguard against inappropriate questions
    banned_words = ["inappropriate", "offensive", "illegal"]  
    if any(word in user_input.lower() for word in banned_words):
        await message.channel.send("I'm sorry, but I can't respond to that request.")
        return

    response = ask_openai(user_input)
    await message.channel.send(response)


# Run bot
client.run(DISCORD_TOKEN)
