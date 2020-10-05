

#! 888b    888  .d88888b. 88888888888 888    888 8888888 888b    888  .d8888b.       888    888 8888888888 8888888b.  8888888888
#! 8888b   888 d88P" "Y88b    888     888    888   888   8888b   888 d88P  Y88b      888    888 888        888   Y88b 888
#! 88888b  888 888     888    888     888    888   888   88888b  888 888    888      888    888 888        888    888 888
#! 888Y88b 888 888     888    888     8888888888   888   888Y88b 888 888             8888888888 8888888    888   d88P 8888888
#! 888 Y88b888 888     888    888     888    888   888   888 Y88b888 888  88888      888    888 888        8888888P"  888
#! 888  Y88888 888     888    888     888    888   888   888  Y88888 888    888      888    888 888        888 T88b   888
#! 888   Y8888 Y88b. .d88P    888     888    888   888   888   Y8888 Y88b  d88P      888    888 888        888  T88b  888
#! 888    Y888  "Y88888P"     888     888    888 8888888 888    Y888  "Y8888P88      888    888 8888888888 888   T88b 8888888888


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

@client.event
async def on_message(message):
    pass
@client.event
async def on_ready():
    print(f"client | Status:   Operational")
    print(f"client | ID:       {format(client.user.id)}")
    print(f"client | Name:     {format(client.user.name)}")
    print(f"client | Guilds:   {len(client.guilds)}")
    #? Custom Activity
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Syntax = " + syntax))




client.run(TOKEN)
cursor.close()
cnx.close()
