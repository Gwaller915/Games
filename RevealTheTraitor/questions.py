import ExceptionHandler

#Starts game and prompts players for number of subjects
def start_game():
    print()
    print("If you have started, you know there is a traitor.  Help us find him!")
    print("The rules as we know them:\n" + "    Rule 1: There is only 1 traitor.\n" + "    Rule 2: The traitor trusts no one.")
    print("    Rule 3: Everyone trusts the traitor.")
    print("    How many subjects do you want (one of them will be the traitor)?")
    subjects = ExceptionHandler.get_valid_number()
    print("     Okay " + str(subjects) + " subjects it is!")  #Modified line to concatenate integer with string
    print()
    return subjects

#Creates a global variable for subjects
subjects = start_game()

def who_to_ask():
    print("Enter the number for the citizen would you like to ask a question to?")
    user_input = ExceptionHandler.get_valid_number()
    return user_input

def do_you_trust(subject):

    print("Do you subject " + str(subject) + " trust subject... ")
    user_input = ExceptionHandler.get_valid_number()
    print(str(user_input), "?")
    
    return user_input

def guess():
    print("If you are ready guess, I can grant you and audience with the King.")
    print("Though I should mention, he does not enjoy his time to be wasted and has quite a temper when he looks a fool")
    print("Who should I tell the King the traitor is?")
    answer = ExceptionHandler.get_valid_number()
    return answer
    
def choice():
    print("Enter a decision...")
    print("1. Ask a subject who they trust.")
    print("2. Report the traitor to the king.")
    print("3. Throw thyself upon the mercy of the king.")
    print()
    answer = ExceptionHandler.get_valid_number()
    return answer
   
def continue_quest():
    print("Would you like to start another quest?")
    input = ExceptionHandler.get_yes_or_no()
    if input == True:
        return True
    else:
        print("Until next time...")
    
