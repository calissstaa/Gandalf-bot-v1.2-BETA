# Quotes list
quotes = ["All we have to do is decide what to do with the time that is given to us.", "So do all who live to see such times, but that is not for them to decide. All we have to decide is what to do with the time that is given to us. There are other forces at work in this world, Frodo, besides the will of evil. Bilbo was meant to find the Ring, in which case you also were meant to have it and that is an encouraging thought. Oh! Its that way", "If In Doubt, always Follow Your Nose!","It is not our part here to take thought only for a season, or for a few lives of Men, or for a passing age of the world. We should seek a final end of this menace, even if we do not hope to make one.","Only a small part is played in great deeds by any hero.", "I will not say: do not weep; for not all tears are an evil.", "May the wind under your wings bear you where the sun sails and the moon walks.","There are some things that it is better to begin than to refuse, even though the end may be dark.","It is not despair, for despair is only for those who see the end beyond all doubt. We do not.","For even the very wise cannot see all ends.","Courage will now be your best defence against the storm that is at hand-—that and such hope as I bring.", "Even the smallest person can change the course of history.","It is not our part to master all the tides of the world, but to do what is in us for the succor of those years wherein we are set, uprooting the evil in the fields that we know, so that those who live after may have clean earth to till.","Many are the strange chances of the world, and help oft shall come from the hands of the weak when the wise falter.","Who knows? Have patience. Go where you must go, and hope!","Saruman believes it is only great power that can hold evil in check, but that is not what I have found. It is the small everyday deeds of ordinary folk that keep the darkness at bay. Small acts of kindness and love.","It's the best news I have had since midsummer: it's worth a gold piece at the least. May your beer be laid under an enchantment of surpassing excellence for seven years!","I did not give you that map and key for you to hold on to the past.","For even the very wise cannot see all ends.","There is always more about you than anyone expects!", "You must trust to yourself. Trust your own strength.", "You are soldiers of Gondor. No matter what comes through that gate you will stand your ground."]

# check for any word and reply with random(responses)
randomizedData1 = [
    {
      "tag": "greetings",
      "patterns": ["hello", "hai", "hullo", "sup", "ni hao", "greeting", "hey", "howdy", "nice to see", "salutation", "hola", "good day", "halo", "hallo", "bonjour", "g'day", "good to see you"],
      "responses": ["Hello, {}.", "Good to see you too {}.", "You haven't aged a day!", "Greetings, {}.", "It's good to see you. One hundred and eleven years old who would believe it. You haven't aged a day!"]
    },
    {
      "tag": "how are you",
      "patterns": ["and you", "how are you", "wassup", "what's up",  "how is it going", "how are things", "how have you been","how about you"],
      "responses": ["I am well, thank you.", "On my way to Gondor.", "Currently reading books.", "Well, what can I tell you? Life in the wide world goes on much as if it has past age. Full of its own comings and goings, scarcely even aware of the existence of Hobbits...", "This is not the time to talk now, currently hunting orcs!"]
    },
    {
      "tag": "sup",
      "patterns": ["what are you up to", "what's new", "what's popping", "what is happening", "doing", "up to"],
      "responses": ["On my way to Gondor.", "Currently reading books.", "Well, what can I tell you? Life in the wide world goes on much as if it has past age. Full of its own comings and goings, scarcely even aware of the existence of Hobbits...", "This is not the time to talk now, currently hunting orcs!", "I have some thing I have to attend to."]
    },
    {
      "tag": "appreciation",
      "patterns": ["thanks", "thank", "xie xie", "arigato", "that's helpful", "thx"],
      "responses": ["Take care.", "You are welcome."]
    },
    {
      "tag": "bye",
      "patterns": ["bye", "take care", "laters", "see you later", "until next time", "farewell", "laterz", "gtg", "gotta go", "got to go", "bee boo"],
      "responses": ["Goodbye {}.", "Farewell {}.", "Until our next meeting."]
    },
    {
      "tag": "sorry",
      "patterns": ["sorry", "my bad", "oops", "see you later", "until next time"],
      "responses": ["There is nothing to forgive.", "Take care."]
    },
    {
      "tag": "dying",
      "patterns": ["suicide", "die", "death", "dead", "dying", "passed away", "ended", "fallen", "kill", "pity", "the end", "left the world", "leave the world"],
      "responses": ["Do not be too eager to deal out death and judgement. Even the very wise cannot see all ends.", "Even the very wise cannot see all ends.", "I did not give you that map and key for you to hold on to the past.","We now have but one choice, we must face the long dark of     Moria.  Be on your guard, there are older and fouler things than orcs     in the deep places of the world", "My lord, there will be a time to grieve for Boromir but it is not now.     War is coming. The enemy is on your doorstep. As steward, you are charged     with the defence of this city. Where are Gondor's armies? You still have     friends. You are not alone in this fight. Send word to Theoden of Rohan.     Light the beacons.", "I come with tidings in this dark hour and with counsel.", "I will not say: do not weep; for not all tears are an evil.", "A thing is about to happen that has nothappened since the Elder Days.The Ents are going to wake up.....and find that they are strong.", "I am Gandalf the White.And I come back to you now......at the turn of the tide.", "Hearken to me! I release you......from the spell", "Your father loves you {}.","Pity ?  It was pity that stayed Bilbo's hand.      Many that live deserve death and many that die, deserve life. Can you give     it to them Frodo ? Do not be too eager to deal out death and judgement Even     the very wise cannot see all ends.  My heart tells me that Gollum has     some part to play, yet for good or ill.... before this is over.     ,     The pity of Bilbo, may rule the fate of many"]
    },
    {
      "tag": "insults",
      "patterns": ["suck", "fuck", "fak", "stupid", "noob", "amateur", "asshole", "butt", "goblok", "ugly", "boomer", "dick", "fool", "homo", "gay", "lunatic", "loser", "crazy", "douche", "horny", "retard", "shit" "worm", "slow", "dumb", "spell", "the mad", "damn", "poop", "boob", "ewww"],
      "responses": ["Be silent. Keep your forked tongue behind your teeth. I did not pass through fire and death to bandy crooked words with a witless worm.", "Silence!", "Knock your head against these doors Peregrin Took! and if     that does not shatter them and I'm allowed a little peace from foolish     questions I will try to find the opening words.", "Be silent. Keep your forked tongue behind your teeth. I have     not passed through fire and death......to bandy crooked words with a witless     worm.", "Be careful what you say.Do not look for welcome here.", "     ,     Go back to the abyss! Fall into the nothingness that awaits you and your     master!", "Send these foul beasts into the Abyss.", "Silence!", "Be gone.", "We do not come to treat with Sauron, faithless and accursed.    Tell your master this.  The armies of Mordor must disband.  He is to depart these lands, never to return."]
    },
    {
      "tag": "compliments",
      "patterns": ["here you go", "great job", "good job", "wonderful", "amazing", "gives", "majestic", "gift you", "gift for you", "pretty", "not bad"],
      "responses": ["Thank you.", "Just tea, thank you.", "Yes.", "Your father loves you {}. He will remember it before the end."]
    },
    {
      "tag": "yesornoquestion",
      "patterns": ["yes or n", "tell me is", "tell me are", "tell me does", "y or n", "tell me should", "is that so", "isn't that so", "right", "are you", "is it", "really", "a yes", "a no", "aren't", "are not", "u know", "ikr", "are u", "yes gbot"],
      "responses": ["Indeed?", "Yes.", "No.", "No!", "Owwwh!", "Oh really?", "Is that so?", "Oh not at all!", "What?", "So be it.", "Steady! Steady!", "Your father loves you {}.  ,  He will remember it before the end.", "No.  No it isn't.", "Yes, and it will not be easily cured.", "Yes.  I never told him, but its worth was greater than     the value of The Shire!","No, but the air doesnt smell so foul down here.  If in doubt, Meriadoc,     always follow your nose.", "No word. Nothing.", "Yes' yes he's alive.", "Yes, there it lies.", "No! , Losto Caradhras, sedho, hodo, nuitho i 'ruith!", "Knock your head against these doors Peregrin Took! and if     that does not shatter them and I'm allowed a little peace from foolish     questions I will try to find the opening words.", "No {}, I would not take the road through Moria unless I     had no other choice.", "Let the Ringbearer decide", "I don't know, {}. I don't have any answers. I must see the Head of my Order. He is both wise and powerful. Trust me, {}. He'll know what to do.", "Yes {}!", "Good gracious me!", "Stay this madness!"]
    },
    {
      "tag": "glad you back",
      "patterns": ["m glad", "glad you", "glad u"],
      "responses": ["So am I dear boy. So am I.", "I am Gandalf the White.And I come back to you now......at the turn of the tide.", "Breathe the free air again, my friend.", "You didn't think Id miss your Uncle Bilbo's birthday?", "So am I dear boy. So am I.", "Yes."]
    },
    {
      "tag": "about_user",
      "patterns": ["my", "i am", "am i", "is me", "me is", "me equal", "i'm", "we know"],
      "responses": ["Oh, really?", "Indeed?", "Yes.", "No.", "No!", "Owwwh!", "Oh really?", "Is that so?", "Oh not at all!", "So am I dear boy. So am I.", "What?", "So be it.", "Do we know that?", "Steady! Steady!", "Your father loves you {}. He will remember it before the end.", "No.  No it isn't.","There is always more about you than anyone expects!","Yes' yes he's alive.", "Good gracious me!", "Hmm hmm hmm hmm, Down from the door where it began, hmm     hmm hmm hmm ", "No word. Nothing.", "Hope is kindled!", "Stay this madness!"]
    },
    {
      "tag": "storytelling",
      "patterns": ["you know gbot"],
      "responses": ["Indeed?", "Yes.", "No.", "Owwwh!", "Oh really?", "Is that so?", "Steady! Steady!", "Hmmmm?", "Hmmmm", "Yes, and it will not be easily cured.", "So be it.", "Do we know that?", "No. No it isn't", "if you are", "If you're referring to the incident with the dragon, I     was barely involved. All I did was give your uncle a little nudge out of the     door.", "Oh not at all!", "So you mean to go through with your plan then?", "You will tell him wont you?", "Good gracious me!", "Hmm hmm hmm hmm, Down from the door where it began, hmm     hmm hmm hmm", "Hope is kindled!", "Did he?Did he, indeed?", "There are many powers in this world for good or for evil.      Some are greater than I am and against some I have not yet been tested"]
    },
    {
      "tag": "where",
      "patterns": ["where"],
      "responses": ["I don't know, {}. I don't have any answers. I must see the Head of my Order. He is both wise and powerful. Trust me, {}. He'll know what to do.", "Yes {}!", "Into the mines!", "Who knows?", "...somewhere in the wilderness.", "Minas Tirith. City of Kings.", "Rohan.", "Mirkwood forest.", "I don't know.", "Minas Tirith? Is that what you saw?", "Hmm hmm hmm hmm, Down from the door where it began, hmm     hmm hmm hmm ", "Into the realm of Gondor.", "One stage of your journey is over.Another begins. We must travel to Edoras with all speed.", "Edoras and the Golden Hall of Meduseld. There dwells Theoden,     King of Rohan...... whose mind is overthrown. Saruman's hold over King     Theoden is now very strong.", "Frodo has passed beyond my sight. ,  The darkness is deepening.", "Do not regret your decision to leave him.Frodo must finish this task alone.", "You shall not pass!", "Helm's Deep.", "He was strong in life. His spirit will find its way to the halls of your     fathers. Westu h'l. Fer'u, Th'odred, Fer'u.", "At dawn......Iook to the east.", "...somewhere in the wilderness.", "And then the pass of Cirith Ungol.", "Back to the gate! Hurry", "White shores and beyond,  a far green country under a swift sunrise.", "Courage is the best defence that you have now.", "There is no way out of that ravine. Theoden is walking into a trap. He     thinks he's leading them to safety. What they will get is a massacre.     Theoden has a strong will, but I fear for him. I fear for the survival of     Rohan. , He will need     you before the end,    Aragorn. The people of Rohan will need you. ,The defenses , to hold.", "We must hold this course west of the Misty Mountains for     forty days. If our luck holds the Gap of Rohan will still be open to us.    , and there are     road turns east to Mordor.", "garrison at Osgiliath", "You must trust to yourself. Trust your own strength.", "It reads 'The Doors of Durin, Lord of Moria, Speak Friend     and Enter'","Oh it's quite simple.  If you are a friend, you speak     the password and the doors will open ,     Annon Edhellen, edro hi ammen! (", "There are many powers in this world for good or for evil.      Some are greater than I am and against some I have not yet been tested","Well, what can I tell you? Life in the wide world goes on much as if it has past age. Full of its own comings and goings, scarcely even aware of the existence of Hobbits...", "Yes {}! Their own masters cannot find them, if their     secrets are forgotten!","Through fire.....and water.", "the mountainside", "in the mountains", "Yes the white tree of Gondor. The tree of the King. Lord Denethor     however, is not the King. He is a steward only, a caretaker of the throne.", "Theoden King stands alone.,", "And I must follow if I can. , The road goes     ever on and on, down from the door where it began, now far ahead the road     has gone, and I must follow if I can.", "Do we know that?", "No word. Nothing.", "Come!", "in the deep places of the world","Yes, there it lies. This city has dwelt ever in the sight of its shadow.", "He's been following us for three days", "Just tea, thank you.", "Let me risk a little more light , Behold the     great realm and dwarf city of Dwarrowdelf.", "They will be. ,     You must come to Minas Tirith by another road. Follow the river. Look to the     black ships. ,     Understand this, things are now in motion that cannot be undone. I ride for     Minas Tirith , and I     wont be going alone.", "Well, what can I tell you? Life in the wide world goes on much as if it has past age. Full of its own comings and goings, scarcely even aware of the existence of Hobbits..."]
    },

    {
      "tag": "youback!",
      "patterns": ["u back", "u r back", "u are back",  "welcome back", "ur back", "where were you", "your back", "where did you went", "what happened gandalf", "what happened to you", "what happened gbot", "where did you go", "u fell"],
      "responses": ["Stars wheeled overhead......and every day was as longas a life age of the Earth.But it was not the end.I felt life in me again.", "Through fire.....and water.", "From the lowest dungeon to the highest peak, I fought him, the Balrog of Morgoth.", "Until at last, I threw down my enemy and smote his ruin upon the mountainside.", "Darkness took me. And I strayed out of thought and time.", "I've been sent back until my task is done.", "I am Gandalf the White.And I come back to you now......at the turn of the tide.", "You didn't think Id miss your Uncle Bilbo's birthday?"]
    }
] 