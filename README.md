<h3 align="center">MySQL Discord Bot</h3>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">Remotely connect to any MySQL Database via Discord and execute any query!
    <br> 
</p>

## About

The MySQL Discord Bot is a powerful tool that allows you to remotely connect to any MySQL database and execute queries directly from a Discord server. This bot is designed to facilitate database management and querying without needing direct access to the database server, making it ideal for developers, database administrators, and technical teams who collaborate on Discord.

## How it works

The MySQL Discord Bot operates by connecting to a MySQL database and executing queries based on user commands within a Discord server. Here’s a step-by-step breakdown of how it functions:

1. **Database Connection**: The bot reads the database connection variables from the vars.py file, which includes the database credentials and connection details.

2. **Command Listening**: The bot continuously listens for specific command syntax in the Discord server. Commands must follow the predefined syntax set in the configuration.

3. **User Authentication**: Upon receiving a command, the bot checks if the user is whitelisted in the vars.py file. Only authorized users are allowed to execute queries.

4. **Query Execution**: If the user is authorized, the bot executes the query on the connected MySQL database.

5. **Response Handling**: The bot sends the query results back to the same Discord channel where the command was issued. If the user is not authorized, the bot sends an error message instead.

## Usage

To use the MySQL Discord Bot, follow these steps:

Command Syntax: All commands must start with the predefined syntax specified in the configuration (e.g., mysql>). This syntax is case-sensitive.
Query Execution: Type your SQL query after the syntax to execute it.
Example:
```shell
mysql> SELECT * FROM `users` WHERE id=2
```
Detailed Steps:
* Whitelisted Users Only: The bot checks if the user issuing the command is whitelisted. If not, an error message will be sent.
* Help Command: Type mysql> help to get a link to MySQL documentation.
* Query Execution: The bot will process the query and return the results. If the query returns an empty list, a message indicating this will be sent. If there is an error in the query, * 

the error message will be displayed.

Responses:
* Successful Query: The bot returns the query results in a tabular format.
* Empty Result: A message indicating that the query returned an empty list.
* Unauthorized User: An error message if the user is not whitelisted.
* Query Error: An error message if there is an issue with the query.

This setup ensures secure and efficient query execution directly from your Discord server.

---

## Getting Started

To set up and run the MySQL Discord Bot, follow these steps:

1. Clone the Repository
Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/YonLiud/MySQL-Discord-Bot/
```

2. Obtain a Discord Bot Token
After cloning the repository, you'll need to obtain a token for your Discord bot. Follow this guide to get your bot token.

3. Install Prerequisites
Before using the bot, install the required Python modules. Navigate to the root directory of the cloned repository and run:

```shell
pip3 install -r requirements.txt
```

4. Configure the Bot
Open the vars.py file located in the root directory of the cloned repository.
Fill in the required information in the vars.py file:
```python
USERNAME = 'your_database_username'
PASSWORD = 'your_database_password'
HOSTNAME = 'your_database_host'
DATABASE = 'your_database_name'
WHITELIST_IDS = [list_of_whitelisted_user_ids]
SYNTAX = 'your_command_syntax'
TOKEN = 'your_discord_bot_token'
```

Replace placeholders (your_database_username, your_database_password, etc.) with your actual database credentials, Discord bot token, and command syntax.

5. Deploying Your Own Bot
To run the bot, execute the following command in your terminal within the root directory of the cloned repository:

```sh
python3 app.py
```


This command starts the MySQL Discord Bot and connects it to your configured Discord server and MySQL database.
