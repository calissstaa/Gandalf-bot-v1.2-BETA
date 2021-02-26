# Quotes list
quotes = ["All we have to do is decide what to do with the time that is given to us.", "So do all who live to see such times, but that is not for them to decide. All we have to decide is what to do with the time that is given to us. There are other forces at work in this world, Frodo, besides the will of evil. Bilbo was meant to find the Ring, in which case you also were meant to have it and that is an encouraging thought. Oh! Its that way", "If In Doubt, always Follow Your Nose!","It is not our part here to take thought only for a season, or for a few lives of Men, or for a passing age of the world. We should seek a final end of this menace, even if we do not hope to make one.","Only a small part is played in great deeds by any hero.", "I will not say: do not weep; for not all tears are an evil.", "May the wind under your wings bear you where the sun sails and the moon walks.","There are some things that it is better to begin than to refuse, even though the end may be dark.","It is not despair, for despair is only for those who see the end beyond all doubt. We do not.","For even the very wise cannot see all ends.","Courage will now be your best defence against the storm that is at hand-—that and such hope as I bring.", "Even the smallest person can change the course of history.","It is not our part to master all the tides of the world, but to do what is in us for the succor of those years wherein we are set, uprooting the evil in the fields that we know, so that those who live after may have clean earth to till.","Many are the strange chances of the world, and help oft shall come from the hands of the weak when the wise falter.","Who knows? Have patience. Go where you must go, and hope!","Saruman believes it is only great power that can hold evil in check, but that is not what I have found. It is the small everyday deeds of ordinary folk that keep the darkness at bay. Small acts of kindness and love.","It's the best news I have had since midsummer: it's worth a gold piece at the least. May your beer be laid under an enchantment of surpassing excellence for seven years!","I did not give you that map and key for you to hold on to the past.","For even the very wise cannot see all ends.","There is always more about you than anyone expects!", "You must trust to yourself. Trust your own strength."]

# check for any word and reply with random(responses)
randomizedData1 = [
    {
      "tag": "greetings",
      "patterns": ["hello", "hai", "hullo", "sup", "ni hao", "greeting", "hey", "howdy", "nice to see", "salutation", "hola", "good day"],
      "responses": ["Hello, {}.", "Good to see you too {}.", "You haven't aged a day!", "Greetings, {}.", "How have you been {}?"]
    },
    {
      "tag": "how are you",
      "patterns": ["and you?", "how are you", "wassup", "what's up",  "how is it going", "how are things", "how have you been","how about you"],
      "responses": ["I am well, thank you.", "On my way to Gondor.", "Currently reading books.", "Well, what can I tell you? Life in the wide world goes on much as if it has past age. Full of its own comings and goings, scarcely even aware of the existence of Hobbits...", "This is not the time to talk now, currently hunting orcs!"]
    },
    {
      "tag": "sup",
      "patterns": ["what are you up to", "what's new", "what's popping", "what is happening", "doing", "up to"],
      "responses": ["On my way to Gondor.", "Currently reading books.", "Well, what can I tell you? Life in the wide world goes on much as if it has past age. Full of its own comings and goings, scarcely even aware of the existence of Hobbits...", "This is not the time to talk now, currently hunting orcs!"]
    },
    {
      "tag": "appreciation",
      "patterns": ["thanks", "thank", "xie xie", "arigato", "that's helpful", "thx"],
      "responses": ["Take care.", "You are welcome."]
    },
    {
      "tag": "bye",
      "patterns": ["bye", "take care", "laters", "see you later", "until next time"],
      "responses": ["Goodbye {}.", "Farewell {}.", "See you again {}.", "Take care, {}.", "Have a good day."]
    },
    {
      "tag": "sorry",
      "patterns": ["sorry", "my bad", "oops", "see you later", "until next time"],
      "responses": ["There is nothing to forgive.", "Take care."]
    },
    {
      "tag": "dying",
      "patterns": ["suicide", "die", "death", "dead", "dying", "passed away", "gone", "fallen", "kill", "pity"],
      "responses": ["Do not be too eager to deal out death and judgement. Even the very wise cannot see all ends.", "Even the very wise cannot see all ends.", "I did not give you that map and key for you to hold on to the past.","We now have but one choice, we must face the long dark of     Moria.  Be on your guard, there are older and fouler things than orcs     in the deep places of the world", "My lord, there will be a time to grieve for Boromir but it is not now.     War is coming. The enemy is on your doorstep. As steward, you are charged     with the defence of this city. Where are Gondor's armies? You still have     friends. You are not alone in this fight. Send word to Theoden of Rohan.     Light the beacons.", "I come with tidings in this dark hour and with counsel.", "I will not say: do not weep; for not all tears are an evil.", "A thing is about to happen that has nothappened since the Elder Days.The Ents are going to wake up.....and find that they are strong.", "I am Gandalf the White.And I come back to you now......at the turn of the tide.", "Hearken to me! I release you......from the spell", "Your father loves you {}.","Pity ?  It was pity that stayed Bilbo's hand.      Many that live deserve death and many that die, deserve life. Can you give     it to them Frodo ? Do not be too eager to deal out death and judgement Even     the very wise cannot see all ends.  My heart tells me that Gollum has     some part to play, yet for good or ill.... before this is over.     ,     The pity of Bilbo, may rule the fate of many"]
    }
]

ifAnyData = [
  {
    "patterns": ["hello", "hai", "hullo", "sup", "ni hao", "greeting", "hey", "howdy", "nice to see", "salutation", "hola", "good day", "evening", "afternoon", "morning"],
    "responses": ["Hello, {}", "Good to see you too {}.", "You haven't aged a day!", "Greetings, {}", "How have you been {}?"]
  },

]

# temp data for ideas
temp1 = {
  "tag": "down_emotions",
  "patterns": ["encourage", "cheer", "sad", "cry", "help", "depres", "confuse", "afraid", "sorrow","stress", "tired", "sedih", "lost", "grieved", "miserable", "trouble", "inspire", "quote", "wisdom"],
  "responses": []
}

temp2 = {
  "tag": "wisdom",
  "patterns": ["inspire", "quote", "wisdom"],
  "responses": []
}