#import the random module
import random
#create a list of words from which a user is to pick
my_list= ['banana','mango','sky','wind','deed','fly', 'future']
#ask the user for their name
name= input('What is your name? ').title()
#Tell them the number of chances they have
print(f'you have 3 chances to guess a random letter from a secret word {name}')
#use the random module to pick a random word of which the user is to guess a letter
rand_word= random.choice(my_list)
#using the list method, separate the letters in the random word
choice= list(rand_word)
#set the initial number of times to 0
count=0
#use a while loop to run the programme a certain number of times
while count<5:
    count+=1
#ask  the user to guess a letter from the list    
    user_guess= input(f'Choose 1 alphabet {name}: ').lower()
    if user_guess in choice:
        print(f'That is correct {name}!!You are so smart')
        print(f'The word is {rand_word}')
        
#break the loop if the player gets it right        
        break
    else:
#run the loop again until the specified condition is not met        
        print('Please try again')
#display the final message if the player does not get the letter right after the specified number of times
if count>=5:
    print(f'The word is {rand_word}')
    print('''You LOOOSEEERRRR!!!
BETTER LUCK NEXT TIME!!''')
