

#! 888b    888  .d88888b. 88888888888 888    888 8888888 888b    888  .d8888b.       888    888 8888888888 8888888b.  8888888888
#! 8888b   888 d88P" "Y88b    888     888    888   888   8888b   888 d88P  Y88b      888    888 888        888   Y88b 888
#! 88888b  888 888     888    888     888    888   888   88888b  888 888    888      888    888 888        888    888 888
#! 888Y88b 888 888     888    888     8888888888   888   888Y88b 888 888             8888888888 8888888    888   d88P 8888888
#! 888 Y88b888 888     888    888     888    888   888   888 Y88b888 888  88888      888    888 888        8888888P"  888
#! 888  Y88888 888     888    888     888    888   888   888  Y88888 888    888      888    888 888        888 T88b   888
#! 888   Y8888 Y88b. .d88P    888     888    888   888   888   Y8888 Y88b  d88P      888    888 888        888  T88b  888
#! 888    Y888  "Y88888P"     888     888    888 8888888 888    Y888  "Y8888P88      888    888 8888888888 888   T88b 8888888888


from re import sub
from columnar import columnar
import os
import mysql.connector
import discord
import vars

whitelisted =  vars.WHITELIST_IDS
syntax = vars.SYNTAX
TOKEN = vars.TOKEN

client = discord.Client()

config = {
  'user': vars.USERNAME,
  'password': vars.PASSWORD,
  'host': vars.HOSTNAME,
  'database': vars.DATABASE,
  'raise_on_warnings': True
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    print("MySQL Connection Created Successfully")
except Exception as e:
    print(e)
    print("Exitting...")
    exit()

def exec(query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return "ERR"
@client.event
async def on_message(message):
    data = []
    query = ""
    if message.author == client.user:
        return
    if message.content.startswith(syntax):
        if message.content==syntax+"help":
            await message.channel.send(embed=discord.Embed(title=client.user.name, description='https://devhints.io/mysql', color=discord.Color.purple()))
            return
        for word in message.content.split():
            query += word + " "
        query = query.replace(syntax, '')
        if(query == " "):
            await message.channel.send(embed=discord.Embed(title=client.user.name, description='Arguments are missing for the query', color=discord.Color.red()))
            return
        output = exec(query)
        if output == "ERR":
            await message.channel.send(embed=discord.Embed(title="An error occurred", description='See console for more information', color=discord.Color.red()))
            return
        for result in output:
            sub_data = []
            for x in result:
                sub_data.append(x)
            data.append(sub_data)
        await message.channel.send(columnar(data, no_borders=False))

@client.event
async def on_ready():
    print(f"bot | Status:   Operational")
    print(f"bot | ID:       {format(client.user.id)}")
    print(f"bot | Name:     {format(client.user.name)}")
    print(f"bot | Guilds:   {len(client.guilds)}")
    print(f"bot Configurations: {config}")
    print(f"Bot is ready to use")
    #? Custom Activity
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Syntax = " + syntax))




client.run(TOKEN)
cursor.close()
cnx.close()
