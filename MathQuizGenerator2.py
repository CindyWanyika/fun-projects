player_name = input("""This is MathQuizGenerator
Please enter your name: """).title()

message = """
Welcome to MathQuizGenerator """
print("Hello" , player_name, message)
#prompt the player to enter the type of operation they want to work with ,addition subtraction,multiplication or division
operation_type= input('please select an operation type: ').lower()
#prompt the player to enter the difficulty level of the questions they want to work on, easy ,medium or hard
difficulty = input('Please select your preferred difficulty level: ').lower()

#create conditionals for the 12 possible sets of choices above
#the first one is addition at an easy level
if operation_type == 'addition' and difficulty=='easy':


    print('Add up the following easy numbers,', player_name)
    #set the initial points to 0
    points= 0
    add1= int(input('What is 1 + 1? '))
    #use an if statement to define the correct answers
    if add1 == 2:
        print('Correct!, You have earned 5 ponts')
        #award 5 points for a correct answer and add it to the innitial
        points += 5
     #define what happens when the player inputs a different answer   
    else:
        print('Not quite right')
        points += 0

    add2= int(input('What is 3 + 2? '))
    if add2 == 5:
        print('Correct!, You have earned 5 ponts')
        points += 5
    else:
        print('Not quite right')
        points += 0

    add3= int(input('What is 2 + 7? '))
    if add3 == 9:
        print('Correct!, You have earned 5 ponts')
        points += 5
    else:
        print('Not quite right')
        points += 0

    add4= int(input('What is 10 + 2? '))
    if add4 == 12:
        print('Correct!, You have earned 5 ponts')
        points += 5
    else:
        print('Not quite right')
        points += 0
        
    print("your total score is ", points)    

#create an if statement for when the user inputs addition as the operation and medium as the difficulty
elif operation_type == 'addition' and difficulty=='medium':

    print(f'Get ready to add the following numbers {player_name} !')
    #set the initial points to 0
    points= 0
    add1= int(input('What is 10 + 16? '))
    #use an if statement to define the correct answers
    if add1 == 26:
        print('Correct! You have earned 10 points')
        #award 10 points for a correct answer and add it to the innitial
        points += 10
     #define what happens when the player inputs a different answer   
    else:
        print('Not quite right')
        points += 0
     #second medium addition question   
    add2= int(input('What is 13 + 20? '))
    if add2 == 33:
        print('Correct! You have earned 10 points')
        points += 10
    else:
        print('Not quite right')
        points += 0
    #third  medium addition question    
    add3= int(input('What is 20 + 700? '))
    if add3 == 720:
        print('Correct! You have earned 10 points')
        points += 10
    else:
        print('Not quite right')
        points += 0
     #fourth medium addition questions
    add4= int(input('What is 100 + 210? '))
    if add4 == 310:
        print('Correct! You have earned 10 points!')
        points += 10
    else:
        print('Not quite right')
        points += 0
    #output the total points earned by the player    
    print(f"Your total score is {points} points!")
    
#create an if statement for when the user inputs addition as the operation and hard as the difficulty
elif operation_type == 'addition' and difficulty=='hard':

    print(f'Get ready to add the following numbers {player_name} !')
    #set the initial points to 0
    points= 0
    add1= int(input('What is 101 + 161 + 52? '))
    #use an if statement to define the correct answers
    if add1 == 314:
        print('Correct! You have earned 20 points')
        #award 20 points for a correct answer and add it to the innitial
        points += 20
     #define what happens when the player inputs a different answer   
    else:
        print('Not quite right')
        points += 0
     #second hard addition question   
    add2= int(input('What is 542 + 1324 + 20? '))
    if add2 == 1886:
        print('Correct! You have earned 20 points')
        points += 20
    else:
        print('Not quite right')
        points += 0
    #third hard addition question    
    add3= int(input('What is 200 + 704 + 111? '))
    if add3 == 1015:
        print('Correct! You have earned 20 points')
        points += 20
    else:
        print('Not quite right')
        points += 0
     #fourth hard addition questions
    add4= int(input('What is 1167 + 2134 + 3003? '))
    if add4 == 6304:
        print('Correct! You have earned 20 points!')
        points += 20
    else:
        print('Not quite right')
        points += 0
    #output the total points earned by the player    
    print(f"Your total score is {points} points!")    
    
#create an if statement for when the user inputs addition as the operation and hard as the difficulty
elif operation_type == 'subtraction' and difficulty=='easy':

    print(f'Get ready to subtract the following easy numbers {player_name} !')
    #set the initial points to 0
    points= 0
    add1= int(input('What is 8-5? '))
    #use an if statement to define the correct answers
    if add1 == 3:
        print('Correct! You have earned 5 points')
        #award 5 points for a correct answer and add it to the innitial
        points += 5
     #define what happens when the player inputs a different answer   
    else:
        print('Not quite right')
        points += 0
     #second hard addition question   
    add2= int(input('What is 20-5? '))
    if add2 == 15:
        print('Correct! You have earned 5 points')
        points += 5
    else:
        print('Not quite right')
        points += 0
    #third hard addition question    
    add3= int(input('What is 13-3? '))
    if add3 == 10:
        print('Correct! You have earned 5 points')
        points += 5
    else:
        print('Not quite right')
        points += 0
     #fourth hard addition questions
    add4= int(input('What is 34-10? '))
    if add4 == 24:
        print('Correct! You have earned 5 points!')
        points += 5
    else:
        print('Not quite right')
        points += 0
    #output the total points earned by the player    
    print(f"Your total score is {points} points!")    
    
    
    
