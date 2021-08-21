
"""
Mariam Ammar
Class: CS 521 - Summer 2
Date: 08/20/21
Final Project 

Defines the 'User' class which
with instance attributes name, close contact, birthday, and mood. 
Includes methods that calculate days till user birthday, 
allow user to generate a madlib, and counts the characters and 
unique words in a journal input. 
"""


from datetime import datetime 


class User():
    '''
    Class with instance attributes name, close contact, 
    birthday, and mood. Includes methods that 
    calculate days till user birthday, allow user to generate
    a madlib, counts the characters and unique words in a journal
    input. 
    ...

    Attributes
    ----------
    self.name : name of user 
    self.__close_contact : close contact of user
    self.birthday = user's birthday 
    self.mood = mood of user 
    self.journal_entry = entry that user inputs into journal
        
    Methods
    -------
    calculate_days_till_bday
    (self, original_date, now = datetime.now()):
        calculate days till birthday of user
        
    mad_lib
    (self, n1, n2, adj1, adj2, adj3):
       Takes words as arguments and outputs
       short madlib poem
    
    __len__():
        calculates characters in user journal input
        
    __repr__():
        prints sentence with user name and mood
        
    __write_in_journal(filename):
        saves user input into specified filename
    '''
    
    def __init__(self, name, close_contact, birthday, mood):
        '''
        Creates class attribute based on
        name, close_contact, birthday, and mood arguments.
        Also defines journal as attribute with empty string
        '''
        self.name = name
        self.__close_contact = close_contact
        self.birthday = birthday
        self.mood = mood
        self.journal_entry = ''
        

    def calculate_days_till_bday(self, birthday, now = datetime.now()):
        '''returns days until birthday argument'''
        delta1 = datetime(now.year, birthday.month, birthday.day)
        delta2 = datetime(now.year+1, birthday.month, birthday.day)
        #if the year has not already passed, use this year
        #else use next year as year value
        #subtract this value from now 
        return ((delta1 if delta1 > now else delta2) - now).days
    
    
    def mad_lib(self, n1, n2, adj1, adj2, adj3):
        '''
        Takes words 5 words as arguments 
        (two nouns and three adjectives) and returns short
        madlib with words as inputs.
        '''
        return f'''
        There was an {adj1} {n1} that lived in a {n2}. She was {adj3},
        lived life without a care, and had very long, {adj2} hair.'''
        
    #magic method
    def __len__(self):
        '''Returns characters in journal_entry attribute'''
        return len(self.journal_entry)
    
    #also a magic method
    def __repr__(self):
        '''Returns sentence with name and mood score of User'''
        return f"{self.name} has a mood score of {self.mood}"
    
    def __write_in_journal(self, text = ' ', file_name = "journal.txt"):
        '''
        Writes journal entry to file along with date and time 
        preceding entry and returns char count and unique words. 
        Uses journal.txt as filename default 
        and creates file if does not exist. Can also take other 
        file_name as argument using keyworld file_name.
        '''
        text = input("\n Go ahead and let your thoughts flow!\n ")
        self.journal_entry = text

        try:
            #Opens file or creates one if file does not exit
            new_file = open(file_name, 'a')
            #No errors should be appear
            #However, included except statement just in case 
        except:
            print("Sorry, something didn't go well.")

        else:   
            #Writes the date and time of entry, along with entry
            new_file.write(f"\n{datetime.now()}\n" + self.journal_entry)
            new_file.close()
            #Creates a list of words then inputs words in a set 
            #To remove duplicate words
            words_lst = set([word for word in self.journal_entry.split()])
            #Return grammatically correct descriptions
            #Based on whether user has more one character/unique word
            if len(words_lst) < 2:
                return\
                f'''
        Wow, that was {len(self)} characters and {len(words_lst)} unique word.
        Great work! You entry was saved in '{file_name}' .
        '''
            else: 
                return \
                f'''
        Wow, that was {len(self)} characters and {len(words_lst)} unique words.
        Great work! You entry was saved in '{file_name}'.
        '''
                        
        
if __name__ == "__main__":
    #Assert calculate days will birthday method is working
    birthday = datetime.now()
    p1 = User("Mariam","Lorena", birthday, 7)
    assert p1.calculate_days_till_bday(birthday) == 364
    
    #Assert madlibs method is working
    n1, n2, adj1, adj2, adj3 = "chair","tree","yellow","angry","hungry"
    assert n1; n2; adj1; adj2; adj3 in p1.mad_lib(n1, n2, adj1, adj2, adj3)
    assert len(p1) == len(p1.journal_entry)
    
    #Assert write_in_journal method working 
    #Requires user input, simply input same input twice
    p1._User__write_in_journal()
    test_file = open("journal.txt")
    test_file_lines = test_file.readlines()
    assert input("Input previous text.") in test_file_lines
    test_file.close()
    
    #Prints User name, mood, and description is all methods properly working
    print(f"{p1} and all methods in the User class are working successfully.")




