import discord, os, random
import mymodule as mdl
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Gandalf"))

# Gandalf names local var
gandalf_names = ["g-bot", "gbot", "gandalfbot", "gandalf bot", "gandalf the bot"]

# Encourage word set
encourage = ["encourage", "cheer", "sad", "cry", "help", "depres", "confuse", "afraid", "sorrow","stres", "tired", "sedih", "lost", "griev", "miserable", "trouble", "inspire", "quote", "wisdom", "counsel", "what should i do", "advice", "sick", "i hate life", "despair", "too hard", "im dead", "how to", ";)", ":)", ";-;", ";_;", ";d", "hope", "dying inside", "dead inside", "frustrat", "desperat"]

# EAster egg dance replies
easterEggDance = ["No.", "There are few who can. The language is that of Mordor, which I will not utter here.", "No!", "Yes.", "Just tea, thank you."]

@client.event
async def on_message(message):
  if message.author.bot:
    return

  # Shortcut for message content
  msg = message.content.lower()
  name = message.author.mention

  # check for gandalf special name calls
  if mdl.specialNameCheck(msg, name):
    await message.channel.send(mdl.specialNameCheck(msg, name))
    return

  # works only when 'gandalf' names is called
  if not any(word in msg for word in gandalf_names):
    return
  
  if any(word in msg for word in encourage):
    text = mdl.get_random_quote()
    await message.channel.send(text)
    return

  if mdl.mainCheck(msg, name):
    await message.channel.send(mdl.mainCheck(msg, name))
    return

  if mdl.withCondition(msg, name):
    await message.channel.send(mdl.withCondition(msg, name))
    return

  listCall = mdl.returnList(msg, name)
  if listCall:
    if listCall["textRep"]:
      await message.channel.send(listCall["textRep"])
    if listCall["gifRep"]:
      await message.channel.send(file=discord.File(listCall["gifRep"]))
    return
  
  # gandalf can dance easter egg ('25'% chance getting)
  if "dance" in msg:
    chance = random.randint(0,100)
    if chance <= 25:
      await message.channel.send(file=discord.File("gifs/gandalf dance.gif"))
      await message.channel.send(file=discord.File("gifs/gandalf hahaha.gif"))
    else:
      await message.channel.send(random.choice(easterEggDance))
    return
  
  # if none of those then generate random reply
  m = mdl.get_random_line()
  if m:
    await message.channel.send(m)
  else:
    await message.channel.send("Hello")

keep_alive()
client.run(os.getenv('TOKEN'))