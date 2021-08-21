"""
Mariam Ammar
Class: CS 521 - Summer 2
Date: 08/20/21
Final Project 
A moodbot program that returns options for a user based
on input relating to their mood. 
"""


from datetime import datetime
import random 
import vlc
from User import User
import sys 
import time

def play_audio(filename):   
    '''
    Takes filename as argument and plays song file
    Allows user to stop song by pressins 's
    '''
    p = vlc.MediaPlayer(filename)
    p.play()
    while True:
        user_input = input("Press 's' to end audio.")
        if user_input == 's':
            return p.stop()
            break
        else:
            print("Sorry, you can only press 's' to stop the audio.")

#Asks user for name and name of friend 
#assigns default values if blank input is given
name = input("Please input your first name.")
if not name:
    name = "my friend"
close_contact = input("Who's your best friend?" or "your best friend")
if not close_contact:
    close_contact = "your best friend"

print(f'''
    Hi {name}! Welcome to be Moodbot.
    We have just a few more questions for you.
    ''')

#Asks for birthday 
#Prompts for user input and reprompts if user input invalid. 
while True:
    year = input('When is your birthday? [YY] ')
    month = input('When is your birthday? [MM] ')
    day = input('When is your birthday? [DD]')

    try:
        year, month, day = int(year), int(month), int(day)
        #Convert into datetime format for parsing later 
        birthday = datetime(year,month,day)
        break

    except:
        print('''
        Sorry, try again! 
        Your number entries must follow the right format.
        ''')


#This while loop allows user to come back to main menu
#each time a selection has been made. 
while True: 
    
#Ask user to rate their mood from 1-10
#Validate input or return error and ask for re-entry
    while True:
        mood \
        = input('''
        Rate the way you feel right now 
        from 1-10 with 10 being the best possible score.
        ''')

        try:
            mood = int(mood)
            #If mood outside of range 1-10, ask user to reinput
            while mood not in range (1,11):
                mood\
                = int(input('''
                    Sorry, try again 
                    and make sure you input a number from 1-10.
                    ''')) 
            break
        #Prints when user does not input a number
        except:
            print('''
            Sorry! Looks like you didn't input a number.
            Please try again.
            ''')
    
    #Assign person as p1 to User class 
    p1 = User(name, close_contact, birthday, mood)
    
    #Menu option selections
    #If users input score 1-5, these selections will be printed
    sad_options = \
    (1, "Listen to a Song"),\
    (2, "Write about it"),\
    (3, "Meditate"),\
    (4, "Read an inspirational quote"),\
    (5, "Get some tips"),\
    (6, "Read a funny poem")
    
    
    #If user inputs a score of 5 or above, these selections printed
    happy_options = \
    (1, "Listen to a Song"), \
    (2, "Write a letter to your future self"), \
    (3, "Take note of some great ideas"), \
    (4, "Plan your birthday celebration"),\
    (5, "Have a dance party"), \
    (6, "Read a fun fact")

    #If mood is 1-2, then user is in critical condition
    #Reminder of closest friend is printed before showing options
    if mood < 3 :
        print(f'''
        Wow. Looks like you're really upset. 
        Make sure to seek out help and think of what {close_contact}
        would think if they knew you were feeling like this!
        How about giving them a call? 
        Or you can...\n
        ''')
        for i in sad_options:
            print(i[0],i[1])
            
            
    #If user inputs score from 3-4, output messsage below with sad options
    if 2 < mood < 5:
        print(f'''
        Why so blue? 
Your birthday is only {p1.calculate_days_till_bday(p1.birthday)} days away!
Prepare a celebration or choose one of the options below.\n''')
        for i in sad_options:
            print(i[0],i[1])
            
    #If mood score > 4 then user is either okay or in good mood. 
    #Print message with happy options
    if mood > 4:
        print('''
        Nice to hear you are at least doing ok!
        Which option would you like to choose?\n
        ''')
        for i in happy_options:
            print(i[0], i[1])
            
    #Prompts user to make selection after options have been printed
    selection = input("Input a number to select an option.")
    #If selection out of option range
    #prompt user to re-input selection
    try:       
        selection = int(selection)
        while selection not in range (1,7):
            selection =             int(input('''Sorry, try again.\n 
            Enter a number according to one of the options.''')) 
            break
    #prints if user does not put number input
    except:
        print("Sorry, try again. You need to input a number.")


    #Tips to be printed if user selects "Get some tips" options
    #Could have been also been defined as list or tuple. 
    tips = \
    {   
     "1. Take a few really deep, controlled breaths.",
    "2. Call a good friend.",
    "3. Go for a walk.",
    "4. Do something outside.",
    "5. Exercise!",
    "6. Eat healthy - food is linked to both physical and mental health.",
    "7. Get at least 8 hours of sleep a day.",
    "8. Make time for yourself and include relaxing rituals into your day.",
    "9. Stay away from smoking and limit your alcohol intake."
    }


    #Inspiration quotes to be printed 
    #based on user selected opion.  
    quotes = \
    [ \
    '''
    \n"To anyone out there who’s hurting 
— it’s not a sign of weakness to ask for help.
It’s a sign of strength." —Barack Obama''',
    "\nThe only time you fail is when you fall down and stay down.",
    "\nEvery day may not be good... but there’s something good in every day.",
    '''\n"Soak up the views. Take in the bad weather and the good weather. 
    You are not the storm." —Matt Haig''',
    "\nA journey of 1000 miles always begins with a single step."
    ]

    #fun facts to be printed based on option
    fun_facts = \
    ("More people get attacked every year by a cow than by a shark.",
     "When you cut a hole in your fishing net, it has fewer holes.",
     "Pennsylvania, USA, has a law which bans you from sleeping on a fridge.",
     "Hot water will turn into ice faster than cold water.",
     "The Mona Lisa has no eyebrows",
     "The entire world's population could fit inside Los Angeles.")

    #Songs to be play based on user selected option and mood. 
    dict_audio = {"sad_song" : "theclimb.mp3", 
              "happy_song" : "toosieslide.mp3",
              "meditation" : "meditation.mp3" , 
              "dance_party" : "dance_party.mp3"}
    
                
    #Output options based on user input if unhappy 
    if mood < 5 and selection == 1:
        play_audio(dict_audio["sad_song"])
    elif mood < 5 and selection == 2:
        
    #Calls method from User class for user to write in journal
        print(p1._User__write_in_journal())
    elif mood < 5 and selection == 3:
        
    #Plays meditation audio
        play_audio(dict_audio["meditation"])
        
    elif mood < 5 and selection == 4:
        #Prints quote at random inded from quotes list
        index = random.randrange(0,len(quotes)-1)
        print(quotes[index])
        
    elif mood < 5 and selection == 5:
        #Prints tips for long-term mental/physical health
        for i in sorted(tips):
            print(i)
            
    elif mood < 5 and selection == 6:
        #Asks for user words to input 
        #User inputs arguments to generate madlib 
        #User madlib method from User class
        while True:
            try:
                n1, n2 \
                = input("Input two nouns with a space in between.")\
                .split()
                adj1, adj2, adj3 \
                = input("Input three adjectives with a space in between.")\
                .split()
            #Prints and allows user to re-input
            #if user inputs incorrect number of values
            except:
                print("Sorry try again.")
            else:
                print(p1.mad_lib(n1, n2, adj1, adj2, adj3)+"\n")
                break

                
    #Actions taken for "Happy" options
    if mood > 4 and selection == 1:
        #Plays "Happy" song
        play_audio(dict_audio["happy_song"])
        
    #Next three options allow user to input entry into journal
    elif mood > 4 and selection == 2:
        print(p1._User__write_in_journal())
    elif mood > 4 and selection == 3:
        print(p1._User__write_in_journal())
    elif mood > 4 and selection == 4:
        #Print statement with days till birthday calculated
        #Then allow for journal entry
        print(f'''
        Wow! 
        Only {p1.calculate_days_till_bday(p1.birthday)} till your birthday.
        How will you celebrate and who will you invite?''')
        print(p1._User__write_in_journal())
        
    elif mood > 4 and selection == 5:
        #Prints string characters with delay to add to mood of option
        strng = "~~~~~~~~~!!!!! ♪┏(・o･)┛♪┗ ( ･o･) ┓♪~~~~~~!!!!~~~~~~"
        for i in strng:
            print(i, end = "")
            time.sleep(0.05)
        #Play dance party audio as soon as string finishes printing
        play_audio(dict_audio["dance_party"])

    #Returns fact at random index
    elif mood > 4 and selection == 6:
        index = random.randrange(0, len(fun_facts)-1)
        print("\n"+fun_facts[index])

    #Allows user to exit program
    #or to go back to mood input to view options list 
    user_input\
    = input\
    ('''
    \nPress 'b' to go back to the main menu 
or another character to exit the program.
    ''')

    if user_input == 'b':
        continue
    else:
        sys.exit(0)

