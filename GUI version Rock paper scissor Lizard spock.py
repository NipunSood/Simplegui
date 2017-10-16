# GUI-based version of RPSLS
# Run code at http://www.codeskulptor.org/

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
def name_to_number(guess):
    if guess=="rock":
        return 0
    elif guess=="paper":
        return 1
    elif guess=="scissors":
        return 2
    elif guess=="lizard":
        return 3
    elif guess=="Spock":
        return 4
    else:
        return "Error: Bad input ",guess," to rpsls"
def number_to_name(no):
    if no==0:
        return "rock"
    elif no==1:
        return "paper"
    elif no==2:
        return "scissors"
    elif no==3:
        return "lizard"
    elif no==4:
        return "Spock"
def output(guess,cno):
    print ""
    print "Player choses",guess
    print "computer choses",number_to_name(cno)
    
    
def RPSLS(guess):
    cno=random.randrange(0,5)
    pno=name_to_number(guess)
    output(guess,cno)
    try:
        tno=(cno-pno)%5
        if tno>=3:
            print "Player Win"
        elif tno==0:
            print "Its A Tie"
        else:
            print "Computers Win"
    except:
        print pno

# Handler for input field
def get_guess(guess):
    RPSLS(guess)


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
