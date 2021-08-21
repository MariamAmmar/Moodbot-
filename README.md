# Moodbot
This was a final project for the Boston University's Information Structure with Python 521 Course.

Having suffered from depression a few years ago, I learned that sometimes the smallest reminders can go a long way in changing your mindset and actions. Although a simple Moodbot program is unlikely to prevent extreme cases from happening, the program aims to include actions that allow a user to reflect on their current situation and, if even slightly, increase the mood of the user by providing options to select that trigger actions based on a mood score that they input.

To run the code one must simply run the main.py file.

The program starts by prompting the user for their name, a close contact, birthday, and to score their current mood from 1-10. Once the user has entered their information, an instance of the class ‘User’ class is created for the user, and methods from this class are used in the main program.

If the user enters a score of 1-2, the name of their close contact is printed to remind the user to consider the feelings of those who care most about them. It then lists a list of options provided for “sad” users. If the user inputs a mood score of 3 or 4, an output with days till their birthday is printed and they are given the same list of options. If a user enters a score of 5 or above, it is likely that the user is either okay or is in a good mood so options for the “happy” user are printed.

The options printed for the user are listed below:
Sad options:
1. Listen to a Song
2. Write about it
3. Meditate
4. Read an inspirational quote 5. Get some tips
6. Read a funny poem

Happy options:
1. Listen to a Song
2. Write a letter to your future self 3. Take note of some great ideas 4. Plan your birthday celebration 5. Have a dance party
6. Read a fun fact

Project files:
User.py
mammar_final.py 
dance_party.mp3 
mediation.mp3 
theclimb.mp3
toosieslide.mp3
journal.txt (created by user)
