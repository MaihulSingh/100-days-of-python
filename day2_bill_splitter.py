# Day 2 – What I learned:
'''
• module
• comment
• variables
• arithmetic operations
• assigenment statement
• input function 
• f-strings for formatting output
• round() function for decimals

'''

import emoji                          # emoji module (Extenral)
print(emoji.emojize(" Welcome to the split the bill Calculator :grinning_face_with_big_eyes::fire:"))

# get user input for bill, tip %, and number of people
bill = float(input("What was the total bill ? :"))
tip = int(input("what percentage tip would you like to give ?\'5%, 10%, 15%, 20%\' : "))
people = int(input("How many people to split the bill"))

tip_percent = tip /100                                     # assignment statement 
total_tip_amount = bill * tip_percent                        
total_bill = bill + total_tip_amount                  
bill_per_persons = total_bill / people                 

final_amount = round(bill_per_persons, 2)                  # round to 2 decimal places

message =f"Each person should pay ${final_amount}"         # create message using f-string

import pyttsx3                                             # pyttsx3 module (External)
print(message)

egnine = pyttsx3.init()
egnine.say(message)
egnine.runAndWait()