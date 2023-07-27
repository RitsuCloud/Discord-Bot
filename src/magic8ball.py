import random

magic8_responds = ["Yes","No", "Signs point to yes", "Signs point to no",
                  "Outlook good", "Outlook not so good", "Ask again later",
                  "Cannot predict now", "Concentrate and ask again",
                  "Better not to tell you now", "Reply hazy, try again",
                  "My reply is no", "My sources say no", "Most likely",
                  "Very doubtful", "It is certain", "It is decidedly so",
                  "Without a doubt", "As I see it, yes","As I see it, no"]

luck_responds = ["Go buy a lottery ticket","Meh", "Good", "AWESOME", "Yikes", 
                 "Pretty bad", "You should probably stay home"]

def magic8():
    return random.choice(magic8_responds)

def luck():
    res = "Your luck today is: " + random.choice(luck_responds)
    return res