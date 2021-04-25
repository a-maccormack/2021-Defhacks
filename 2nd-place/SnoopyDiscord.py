import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Good Grief!')

sad_words = ["sad", "depressed", "unhappy", "stressed", "angry", "miserable", "depressing", "upset", "helpless","hopeless", "dumb"]

starter_encouragements = [
  "Cheer up! There is light ahead the tunnel.",
  "Hang in there, help is coming!",
  "You are a great person!",
  "Don't say that, I love you",
  "I care about you"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content

  if msg.startswith(':)snoopylaugh'):
    await message.channel.send('https://tenor.com/view/giggle-snoopy-laugh-happy-gif-14140301')

  if msg.startswith(':0'):
    await message.channel.send('https://tenor.com/view/dancing-snoopy-happy-feet-sunglasses-gif-11305262')

  if msg.startswith(':)snoopydance'):
    await message.channel.send('https://tenor.com/view/snoopy-dance-happy-emotion-response-gif-7404986')

  if msg.startswith(':)purpose'):
    await message.channel.send('My purpose is to try and make you smile. I have a lot of ways to do that! Times are tough right now, and why not burn some of it smiling? Hope you enjoy using the Snoopy Bot!')

  if msg.startswith(':)help'):
    await message.channel.send('These are all of the things I can do - **:)hello, :)inspire, :)add *encouragement*, :)del *encouragement*, :)list encouragements, :)responding true, :)responding false, :)snoopylaugh, :)snoopydance, :)purpose, :)lie, :)snoopysurprised, :)peanuts-song.** Thank you for using the Snoopy Bot!')

  if msg.startswith("ping"):
    await message.channel.send("Pong!")

  if msg.startswith(":)lie"):
    await message.channel.send("I do not like you")

  if msg.startswith("Thank you Snoopy"):
    await message.channel.send("You are welcome :D")

  if msg.startswith("thank you snoopy"):
    await message.channel.send("You are welcome :D")

  if msg.startswith("THANK YOU SNOOPY"):
    await message.channel.send("You are welcome :D")

  if msg.startswith(":)peanuts-song"):
    await message.channel.send("https://www.youtube.com/watch?v=jPgewHpf-q4")

  if msg.startswith("xue hua piao piao"):
    await message.channel.send("https://www.youtube.com/watch?v=W8x4m-qpmJ8")

  if msg.startswith("Ping"):
    await message.channel.send("Pong!")

  if msg.startswith(":("):
    await message.channel.send("Cheer up!")
  
  if msg.startswith("D:"):
    await message.channel.send("Cheer up!")

  if msg.startswith(":)snoopysurprised"):
    await message.channel.send("https://tenor.com/view/snoopy-gif-8753989")

  if msg.startswith("i am hungry"):
    await message.channel.send("I'll make you peanuts :D")

  if msg.startswith(':)hello'):
    await message.channel.send('Hi!')

  if msg.startswith(':)hi'):
    await message.channel.send('Hello!')
  
  if msg.startswith(':)inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith(':)'):
    await message.channel.send(':D')

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options +=db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith(":)add"):
    encouraging_message = msg.split(":)add ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouragement added!")
  
  if msg.startswith(":)del"):
    encouragements = []
    if "encouragements" in db.keys():
     index = int(msg.split(":)del",1)[1])
     delete_encouragement(index)
     encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    await message.channel.send("Encouragement deleted!")

  if msg.startswith(":)list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith(":)responding"):
    value = msg.split(":)responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding on!")
    else:
      db["responding"] = False
      await message.channel.send("Responding off!")

keep_alive()
client.run(os.getenv('TOKEN'))