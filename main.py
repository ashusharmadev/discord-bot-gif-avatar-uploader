import discord

intents = discord.Intents(
    guilds=True,
)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Connected to bot.")
    print("Uploading the avatar...")
    try:
        with open("avatar.gif", 'rb') as avatar:
            await client.user.edit(avatar=avatar.read())
        print("Upload success.")
    except Exception as e:
        print("Failed to upload : ", e)


bot_token = input("Your discord bot token: ").strip()

client.run(bot_token)
