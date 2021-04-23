<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://icons-for-free.com/iconfiles/png/512/development+logo+mysql+icon-1320184807686758112.png" alt="Bot logo"></a>
</p>

<h3 align="center">MySQL Discord Bot</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 Remotely connect to any MySQL Database and execute any query!
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Deploying your own bot](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

The bot 

## 💭 How it works <a name = "working"></a>

The Bot first connect to the database by reading the variables in ``vars.py`` and execute a connection query.

After that the bot will be listening to commands starting with the query, on command syntax it will run a check, if the user executing the query is whitelisted in the ``vars.py`` file, if the person is authorized, the query will be executed

If not, the query will not be executed and the bot will send an error message to the same channel of execution of command

The entire bot is written in Python 3.8

## 🎈 Usage <a name = "usage"></a>

To use the bot, type:

```
<syntax you set> <query>
```

The first part, i.e. "<syntax>" **is** case sensitive.

### Example:
```
mysql> SELECT * FROM `users` WHERE id=`2`
```

---

## 🏁 Getting Started <a name = "getting_started"></a>

first clone the repository into your local machine!
```sh
git clone https://github.com/YonLiud/MySQL-Discord-Bot/
```
after cloning, you need a token for your discord bot, please follow [this guide](https://www.writebots.com/discord-bot-token/) how to get one



### Prerequisites

You will need to install some modules before being able to use the bot!

```shell
pip3 install -r requirements.txt
```
### Installing

Now we need to configure the bot!

Now open ``vars.py`` file located in the root directory of the clone

Insert into the required fields the required information

## 🚀 Deploying your own bot <a name = "deployment"></a>

To run the bot, simply execute a python3 command!
```sh
python3 app.py
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Visual Studio Code](https://github.com/microsoft/vscode) - free source-code editor made by Microsoft for Windows, Linux and macOS

## ✍️ Authors <a name = "authors"></a>

- [@YonLiud](https://github.com/YonLiud) - Idea & Initial work
