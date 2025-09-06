# Day 1 What i learned on the day 1 
'''
• module
• comment
• input
• variables

'''
import pyjokes                                                                # Module (External)
import pyttsx3 

print("Let ask some question")

name = input("What's your name ? ")                                           # Take the input from the user
print("Is your name is ? :", name)

age = input("What your age ? ")                                                # Take the input from the user
print("Is your age is ? : ", age)

print("Your name is: ", name)
print("And your age is: ", age)
 
import emoji                                                                    # emoji module (External)
print(emoji.emojize("You wanna hear a joke :grinning_face_with_big_eyes:"))

joke = pyjokes.get_joke()                                                       # pyjokes module (External)    
print(joke)

egnine = pyttsx3.init()                                                         # pyttsx3 module (External) 
egnine.say(joke)
egnine.runAndWait()