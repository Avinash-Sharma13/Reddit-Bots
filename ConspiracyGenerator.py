import praw
import random
import time
import os
from config import *

def login():
    print("Loggin in...")
    reddit = praw.Reddit(client_id = client_id,
                         client_secret= client_secret,
                         username= username,
                         password= password,
                         user_agent= user_agent)
    print("Logged in!")
    return reddit

reddit = login()
subreddit = reddit.subreddit("insanepeoplefacebook")

phrase = "!createconspiracy"

def Generator():

    Who = ["The government", "Bill Gates and his Cohort", "Immigrants", "The Gays", "Doctors", "People",
           "The Japanese", "Corporations", "Atheists", "NASA", "Liberals", "Facebook", "Lizard People",
           "Morning news"]

    How = ["the TV", "Abortions", "Nanotechnology", "Satan", "Video Games", "Feminism", "Pesticides",
           "The sun's rays", "Dihydrogen Monoxide", "Lies and Propaganda", "GMOs",
           "Vaccinations", "Holographic Simulations", "Deep Drilling", "High-Fructose Corn Syrup", "Realistic Clones"]

    What = ["cause Cancer", "give childeren autism", "erode your brain", "turn people gay", "make you fat",
            "amass enormous wealth", "cause global warming", "destroy America", "turn you into a sheep",
            "kill the bees at an alarming rate", "take over the world", "hide the Aliens",
            "Communicate with dolphines", "bring back MJ"]

    choiceWho = random.choice(Who)
    choiceHow = random.choice(How)
    choiceWhat = random.choice(What)

    if (choiceWho == "The Government" or choiceWho == "NASA"
        or choiceWho ==  "Facebook" or choiceWho ==  "Morning News"):

        return choiceWho + " is Using " + choiceHow + " to " + choiceWhat
    else:
        return choiceWho + " Are Using " + choiceHow + " to " + choiceWhat


def run(reddit, idList, botComment):
    print("Obtaining 50 Comments...")
    for comment in subreddit.comments(limit = 50):
        if phrase in comment.body and comment.id not in already_replied_to and comment.author != reddit.user.me():
            try:
                print(f"String with {phrase} found in Comment "+ comment.id)
                comment.reply(botComment)
                print("Replied to Comment: "+ comment.id)
                already_replied_to.append(comment.id)
                with open("Comments_replied_to.txt", "a") as f:
                    f.write(comment.id +  "\n")
                break
            except Exception as e:
                print(e)
    print("sleeping for 1min seconds ")
    time.sleep(25)

def get_saved_comment():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    with open("Comments_replied_to.txt", "r+") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
    return comments_replied_to

already_replied_to = get_saved_comment()
print(already_replied_to)

while True:
    botComment = Generator()
    print(botComment)
    print(already_replied_to)
    run(reddit, already_replied_to, botComment)
