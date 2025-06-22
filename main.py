# a basic chat bot code in python 
import os
import json
import random
from textblob import TextBlob

current_dir=os.path.dirname(__file__)
file_path= os.path.join(current_dir,"features.json")

try:
    with open(file_path, "r")as file:
        data=json.load(file)
except Exception as e:
    print(e)
    
    # This function detects mood and suggest activity    
def detect_mood(mood):
    try:
        blob = TextBlob(mood)   
        polarity= blob.sentiment.polarity
        if polarity> 0.3:
            return "positive"
        elif polarity < -0.3:
            return "negative"
        else:
            return "neutral"
    except Exception as e:
        print("Mood detection error:", e)
        return "neutral"  
    
    # this function is for basic guess the number game.
def guess_num():
    try:
        num_guess=int(input("Guess a number between 0 to 10 "))
        num=random.randint(0,10)
        
        if(num_guess==num):
            print("Correct Answer! I guessed ",num)
        else:
            print("You lose! I guessed ",num)
            
    except ValueError:
        print("Enter a valid number ! ")
        
    # this function is for basic game if user ask for rock,paper,scissor game
def rock_paper():
    try:
        options=["rock","paper","scissor"]
        user_ans=input("Enter Your choice: ").lower().strip()
        bot_ans=random.choice(options)
        if(bot_ans=="rock" and user_ans == "scissor"):
            print("Bot wins! Rock beats Scissor. ")
        elif(bot_ans == "scissor" and user_ans =="paper"):
            print("Bot wins! Scissor beat paper. ")
        elif(bot_ans == "paper" and user_ans =="rock"):
            print("Bot wins! Paper beats rock. ")
        elif(user_ans!="rock" and user_ans!="scissor" and user_ans!="paper"):
            print("Invalid answer! select rock, paper or scissor")
        else:
            print("Yes! you win. ")
    except Exception as e:
        print(e)
       
    # this function gives answer using key-words used in user input       
def bot_answer(user_input):
    try:
        if ( "hi" in user_input or "hello" in user_input or "hey" in user_input ) :
            print("Bot : Hello! How are you ? ")
            
        elif ("bye" in user_input or "good bye" in user_input or "okay, talk you later" in user_input ):
            print("Bot: Okay , Bye! Take care")
            return False
            
        elif (" tell a joke" in user_input or "joke" in user_input ):
                print ("Bot : ", random.choice(data["jokes"]))
                
        elif (" tell a fact" in user_input or "fact" in user_input ):
                print ("Bot : ", random.choice(data["facts"]))
                
        elif ("wow" in user_input or "hurrah" in user_input  or "haha" in user_input or "good one" in user_input):
            print("Haha! ")
            
        elif ("really"in user_input or "oh okay" in user_input or "oh" in user_input or "okay" in user_input or "ok" in user_input):
            print("Yes!")
        
        elif ("ugh" in user_input or "ahh" in user_input or "argh" in user_input or"urgh" in user_input or "uff" in user_input or "annoying" in user_input or "tired" in user_input):
         print("Bot: Oh no! Sounds like you're frustrated. \n Want to play a game or hear a joke to cheer up?")
         
        elif("smart"in user_input or "nice" in user_input or "good job" in user_input):
            print("Thanks! You are awesome and gentle. ")
            
        elif("who are you" in user_input or "what are you" in user_input or "your name" in user_input or "how are you" in user_input):
            print("I'm just a simple chat bot made of python. \n   sssh! And secret is that I will be updated too")
            
        elif ("what can you do" in user_input or "what you can do" in user_input or "services" in user_input or "entertain me" in user_input or "how you work" in user_input):
            print("I can tell you a joke,or fact, play number guessing game , rock paper scissor game even can ask you riddle.")
            
        elif ("tell me riddle" in user_input or "riddle" in user_input):
            key = random.choice(data["riddles"])
            user_guess=input(key["question"]).lower().strip()
            print("")
            if (user_guess == key["answer"].lower().strip()):
                print("Bot : Correct! The answer is ",key["answer"])
                
            else:
                print("Bot : Wrong ! The answer is ",key["answer"])
                
        elif("number game"in user_input or "guess number"in user_input or"number guess"in user_input or "number guess game"in user_input  ):
            guess_num()
        
        elif("rock" in user_input or "paper" in user_input or "scissor" in user_input or "rock paper game" in user_input ):
            rock_paper()
        
        else:
            print("Sorry! I couldn't understand. \n I can tell you a joke or fact, play number guessing game ,rock paper scissor game or even ask you riddle.\n What do you want?")
            
    except Exception as e :
        print(e)
        
    return True


print("WELCOME TO BASIC CHAT BOT: ")   
#This will greet and detect mood of user
print("Hi! How are you? ")

mood = input("you: ").lower().strip()

result=detect_mood(mood)

if result=="positive":
    print("BOT : Oh great ! So let's chat.")
    print("\n Suggestion: you can watch movie , read book or go for outing to keep feeling happy ! ")
elif result =="negative":
    print("Oh! you sound low. How can I help you? Do you want to hear a joke or play a game? ")
    print("Suggestion:  you can have a talk with your friend to cheer your mood or go for walk or movie.")
else:
    print("Bot: Got it. I'm here to help or entertain you.")
    print("Suggestion:  you can have a talk with your friend , go for walk or movie, read book or go for outing to cheer your mood .")
    

# through while loop , chatbot continues chat 
    
while True:
    user_input=input("You : ").lower()
    cont=bot_answer(user_input)
    if not cont:
        break