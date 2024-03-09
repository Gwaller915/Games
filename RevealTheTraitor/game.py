import random
import questions

#Global variables
guess = False
turn = 0
subjects = questions.subjects

#Detemines the traitor
def this_is_the_traitor(subjects):
    traitor = random.randint(1, subjects)
    return traitor

#Global variable for traitor
traitor = this_is_the_traitor(subjects)

#Creates a list of all the trusting subjects
def subjects_who_trust(subjects, traitor):
    trusting = []
    for i in range (1, subjects + 1):
        trusting.append(i)
    trusting.remove(traitor)
   #print("The trusting subjects are: " + str(trusting))
    return trusting
 
#Global variable for list of subjects who trust
trusting = subjects_who_trust(subjects, traitor)

#Creates a list of all the trusted sbujects
def subjects_who_are_trusted(subjects, traitor):
    trusted = []
    trusted.append(traitor)
    trusted_generator = random.randint(1, subjects)
    if trusted_generator > subjects - 1:
        trusted_generator = subjects - 1
    trusted_subjects = random.sample(range(1, subjects), trusted_generator)
    #print("The trusted subjects are : " + str(trusted_subjects))
    return trusted_subjects

#global variable for list of subjects who are trusted
trusted = subjects_who_are_trusted(subjects, traitor)

#Creates a dictionary of all the subjects where trusting subject is key and trusted is value  
def who_trusts_who(trusting, trusted, traitor):
   
    trusting_to_trusted = {}
    for citizen in trusting:
        random_trusted_generator = [random.randint(1, len(trusted)) for _ in range(len(trusted))]
        #print(random_trusted_generator)
        trusting_to_trusted[citizen] = set(random_trusted_generator)
        trusting_to_trusted[citizen].add(traitor)
        #print(trusting_to_trusted)
     
    #print(trusting_to_trusted)
    return trusting_to_trusted

who_trusts_who = who_trusts_who(trusting, trusted, traitor)

#Prints trusted list, trusting list and traitor     
def cheat(subjects, traitor, trusting, trusted):
    trusted_subjects = subjects_who_are_trusted(subjects, traitor)
    traitor = this_is_the_traitor(subjects)
    trusting = subjects_who_trust(subjects, traitor)
    print("The trusted subjects are : " + str(trusted_subjects))
    print("The trusting subjects are: " + str(trusting))

#Gives up and ends game    
def give_up(traitor): 
    print("The traitor is subject number: ", traitor)

def win(subject, traitor):
    if subject == traitor:
        print("You have sucessfully identified the traitor. The King has invited you to a feast in your honor!")
        print("Winner! Huzzah!")
        return True
    if subject != traitor:
        print("You have unsucessfully indentified the traitor.")
        print("This has caused the King to lose faith in you.")
        print("And it pains my to tell you but the King has sentenced you to death")
        print("Your failure will have your family for generations...")
        print()
        return True

def kings_mercy():
    kings_ruling = random.randint(1,3)
    if kings_ruling == 1:
        print("The King has taken mercy on your and will allow you live, though without your tongue.")
    elif kings_ruling == 2:
        print("The combination of your lack of effort and intelligence has enraged the King.")
        print("He has summoned the Executioner...")
    elif kings_ruling == 3:
        print("The king has taken pity on your weak will.  He will allow you to live, for now.")
    print()    
    print("Your quest has ended.")
    print() 
    return True

