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
    print("Error at:")
    print(e)
    print()
    print("Exiting...")
    exit()

def exec(query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        return str(e)
        #return ['ERR', e]
@client.event
async def on_message(message):
    data = []
    query = ""
    if message.author == client.user:
        return
    if message.content.startswith(syntax):
        if message.author.id not in whitelisted:
            await message.channel.send(embed=discord.Embed(title="You are not authorized to use this bot", description='Please contact the bot hoster to add you to the whitelisted members list', color=discord.Color.red()))
            return
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
        if output == []:
            msg = await message.channel.send(embed=discord.Embed(description="Empty list returned", color=discord.Color.blue()))
            return
        if isinstance(output, list):
            for result in output:
                sub_data = []
                for x in result:
                    sub_data.append(x)
                data.append(sub_data)
            await message.channel.send(columnar(data, no_borders=False))
            # await message.channel.send(output)
            return
        else:
            msg = await message.channel.send(embed=discord.Embed(title="MySQL Returned an Error", description=output, color=discord.Color.orange()))
            await msg.add_reaction("⚠️")
            return
@client.event
async def on_ready():
    print(f"Bot | Status:   Operational")
    print(f"Bot | ID:       {format(client.user.id)}")
    print(f"Bot | Name:     {format(client.user.name)}")
    print(f"Bot | Guilds:   {len(client.guilds)}")
    print(f"Bot Configurations set to:\n{config}")
    print(f"Bot is ready to use")
    #? Custom Activity
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Syntax = " + syntax))
client.run(TOKEN)
