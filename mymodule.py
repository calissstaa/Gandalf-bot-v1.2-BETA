import requests
from random import choice
from os import getenv
import mydata as dt

def mainCheck(text, name):
  for i in range (len(dt.randomizedData1)):
    temp = []
    for j in dt.randomizedData1[i]["patterns"]:
        temp.append(j)

    if any(word in text for word in temp):
      return choice(dt.randomizedData1[i]["responses"]).format(name)
  
  return None

def specialNameCheck(text1, name): 
  switcher = { 
      "gandalf": "Gandalf? Yes... that was what they used to call me. Gandalf the Grey. That was my name.", 
      "gandalf...": "I am Gandalf the White. And I come back to you now - at the turn of the tide.",         "gandalf?": "Yes, I'm here and you're lucky to be here, too. A few more hours and you would have been beyond our aid. You have some strength in you my dear Hobbit.",
      "gandalf!":"{}.".format(name),
      "olorin": "How did you come to know that name?",
      "tharkun": "Are you a realtive of dwarves?",
      "incanus": "Long have someone called me by that name",
      "stromcrow": "I will draw you, Saruman, as poison is drawn from a wound."
    } 
  return switcher.get(text1, None) 

# Constant Data Checker 
"""
For:
- same answers/replies 
- 'all' included in list 
- formats 
- pics/gifs reply
"""
constDC = {
  "timePeriod": ["morning", "evening", "afternoon"],
  "youLate": ["u", "r", "late"],
  "gg": ["lol", "hahaha", "well played"],
  "up_emotions": ["happy", "cheer", "yay", "wow","excite", "awesome"],
  "angry_emotions": ["grrr", "roar", "argh"]
}

def withCondition(text, name):
  
  if "pass" in text:
    return "You... Shall not, pass!"

  elif "good night" in text or "goodnight" in text:
    return "Good Night {}.".format(name)
  
  elif "i wish" in text:
    return "So do all who live to see such times, but that is not for them to decide. All we have to decide is what to do with the time that is given to us."

  elif "good" in text:
    if " " in text:
      spl = text.split()
      next_word = spl[spl.index("good") + 1]
      if any(word in next_word for word in constDC["timePeriod"]):
        return "What do you mean? Do you wish me a good {t}, or mean that it is a good {t} whether I want it or not; or that you feel good this {t}; or that it is a {t} to be good on?".format(t = next_word)
  else:
    return None

# return multiple values usually with 2 (for gifs)
def returnList(text, name):
  tmp = {
    "textRep": None,
    "gifRep": None
  }

  if all(word in text for word in constDC["youLate"]):
    tmp["textRep"] = "A wizard is never late, {}. Nor is he early; he arrives precisely when he means to.".format(name)
    tmp["gifRep"] = "gifs/precisesly_;3.gif"
    return tmp
  
  elif any(word in text for word in constDC["gg"]):
    tmp["gifRep"] = "gifs/faster wink.gif"
    return tmp
  
  else:
    return None


# Return random movie lines
def get_random_line():
  
  key = "Bearer {}".format(getenv('API_KEY'))

  url = requests.get("https://the-one-api.dev/v2/quote?character=5cd99d4bde30eff6ebccfea0", 
  headers ={
        "Authorization": "Bearer _ZV4QrtOiART2dX9fEKp"
  })

  data = url.json()

  list1 = []
  for i in data["docs"]:
    word = ""
    for j in i["dialog"]:
      word = word + j
    list1.append(word)
  
  # return the value
  return choice(list1)

def get_random_quote():
  holder = dt.quotes
  return choice(holder)
