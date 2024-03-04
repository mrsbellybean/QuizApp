import string
import random
import pprint

qanda = {1: 'Which gas do plants primarily use for photosynthesis?',
         2:'Who painted the famous work \"Starry Night\"?',
         3:'What is the capital of Australia?',
         4:'Which planet is known as the \"Red Planet\"?',
         5:'Who is the author of \"To Kill a Mockingbird\"?',
         6:'What letters represent gold on the periodic table?',
         7:'In Greek mythology, who is the god of the sea?',
         8:'What does the \"www\" stand for in a website browser?',
         9:'What is the smallest country in the world?',
         10:'What is the largest organ in the human body?'}
answers= {1:'carbon dioxide',
          2:'vincent van gogh',
          3:'canberra',
          4:'mars',
          5:'harper lee',
          6:'au',
          7:'poseidon',
          8:'world wide web',
          9:'vatican city',
          10:'skin'} 

user_scores = {}

def randomise(randomisation, keylist):
    if randomisation == 'y':
        print (keylist)    
        random.shuffle(keylist)                                                                           #Shuffle this list to ask the questions in a random order

        print (keylist)
        user_score = 0
        correct_answers = {}
        incorrect_answers = {}
    
    else:
        return (keylist)
    return (keylist)


def run_quiz():
    print('Welcome to the best quiz')                                                                               #Welcome message
    username = input('Please enter your name\n\t')
    while ((type(username)!=str) or (len(username)==0) or (username==" ")):                                         #Check that the username is valid
        username = (input('Please enter a valid name\n\t'))
                    
    no_questions = int(input('How many questions would you like to answer? Please enter a value from 1 to 10\n\t')) #Convert the user's desired number of questions to an integer value to check is it's valid
    while ((type(no_questions)!=int) or (no_questions<1) or (no_questions>10)):                                     #Check that the number of questions entered is valid
        no_questions = int(input('Please enter an integer value from 1 to 10\n\t'))
    else:
        no_questions = no_questions+1                                                                               #Increase the integer by 1 because loops iterate up until this exclusive value            

    keylist = []
    for j in range (1, (no_questions)):
        keylist.append(j)                                                                                       #Populate a list for the keys (question numbers) of the Q&A dictionary
    
    randomisation = input("Would you like to randomise the questions? Press y or n.\n If incorrect input is entered, system will not ask questions randomly...\n\t ")
    randomisation = randomisation.lower()
    randomise(randomisation, keylist)

    user_score = 0
    correct_answers = {}
    incorrect_answers = {}
    
    for i in keylist:                                                                               #Iterate through the random order of questions using the shuffled keys list
            print (qanda[i])                                                                                      #Print the question with the key value of i
            answer = input()
            while ((answer==" ") or (len(answer)<1)):                                                               #check that the answer is not left blank
                print (qanda[i])
                answer = input()
                answer = answer.lower()                                                                             #Convert the user's answer to lowercase so it matches the dictionary's answer
            if answer == answers[i]:
                print('Correct!')
                user_score = user_score + 1                                                                     #If answer is correct, increase the user's score by 1 and print 'Correct!'  and store the correct answer in a dictionary of correct answers
                correct_answers.setdefault(i,answer)
            else:
                print('Incorrect!')                                                                             #If answer is incorrect, print 'Incorrect!' and store which number was incorrect in a dictionary of incorrect answers
                incorrect_answers.setdefault(i,answers[i])
                
    user_percentage = round((user_score/(no_questions-1)*100))
    print ('You got ', user_score, ' answers correct, giving you a percentage score of ', user_percentage, '%!')
    print ('The answers you got correct were:')
    pprint.pprint(correct_answers)
    print ('The answers you got incorrect are below, along with the correct answers:')
    pprint.pprint(incorrect_answers)
    user_scores.setdefault(username, user_percentage)                                                               #Store the user's name along with their percentage score in the dictionary 'user_scores'
        


def continue_quiz():
    cont = input('Does anyone else want to do the quiz? y = yes, n = no\n\t')
    while cont == 'y':
        run_quiz()
        cont = input('Does anyone else want to do the quiz? y = yes, n = no\n\t')
    else:
        print('Thank you for doing the quiz!!')

def display_scores():
    print("Here are all the users\' scores:")
    for key in user_scores:
        print(key, " scored:")
        print (user_scores.get(key))

def highest_score():
    max_score = 0                                                                                                   #Initialise the maximum score to 0 (so that the first value will be the maximum score)
    for key in user_scores:
        score = user_scores.get(key)
        if score>max_score:                                                                                         #Iterate through the dictionary, replacing the higher value with the maximum score
            max_score = score
            best_player = key                                                                                       #Store the player with the highest score
        
    print ("The best player was ", best_player, ", who scored ",max_score,"%")
    
def average_score():
    total_scores = 0
    no_users = len(user_scores)
    for key in user_scores:
        total_scores += user_scores.get(key)
    average_score = round(total_scores/no_users)
    print ("The average score for the group was ",average_score,"%")
        
run_quiz()
continue_quiz()
display_scores()
highest_score()
average_score()

