import random
list = []
list2 = []

score = 0
def read_file():
    '''
    Reads contents from the text file (questions.txt)
    @return a list of five random questions
    '''
    
    with open('questions.txt') as f:
        i = 1
        for line in f.readlines():
            split = line.split(",")
            list.append(split)
            print(str(i)+"."+line)
            i+=1
        #print(list)
        questions_list = []
        while len(questions_list) < 5:
            res = random.sample(list, 5)
            questions_list = [l for b, l in enumerate(res) if l not in res[:b]]
            
        print("***********************************")
        print("new list : "+ str(questions_list))
        print("***********************************")
        print("new list length : "+ str(len(questions_list)))
        ask_questions(questions_list)
        
        while 5-len(list2)< 5:
            print("\nYour score is "+str(5-len(list2))+"/5\n")
            ask_questions(list2)

        print("\nYour score is "+str(5-len(list2))+"/5\n")
        print("------------------------------------------")
        print("            You have passed!!!")
    


def ask_questions(list_of_questions):
    '''
    Sends quesions one at a time to be displayed
    @param list of five questions
    @return a list of questions the user answer incorrectly
    '''
    
    
    j = 1
    for x in list_of_questions:
        answer = str(x[1]).strip()
        print(str(j)+". "+x[0])
        print(x[2])
        print(x[3])
        print(x[4])
        print("")
        print("Enter your answer")
        userInput = str(str(input()).upper().strip())
        is_correct_answer(answer, userInput, x)
        
        j+=1

def display_question(question_number, question):
    '''
    Displays a single question from the list of questions
    Takes in an answer
    @param a single question
    @return the answer given by the user
    '''


def is_correct_answer(solution, user_answer, x):
    '''
    Checks if the answer given by the user is correct
    @param solution - The correct answer
    @param user_answer - The answer entered by the user
    @return boolean indicating if user answered correctly or not
    '''

    if solution == user_answer:
        print("CORRECT")
        if x in list2:
            list2.remove(x)
    if solution != user_answer:
        list2.append(x)
        print("INCORRECT")


def next_round(current_round):
    '''
    Calculates the next round
    @param current round completed
    @return integer next round
    '''


if __name__ == '__main__':

    #score = 0
    #current_round = 0
    #question_list = read_file()

    #while score < 5:
        #current_round = next_round(current_round)
        #question_list = ask_questions(question_list)
        #score = 5 - len(question_list)


    read_file()