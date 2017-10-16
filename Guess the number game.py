# Run code at http://www.codeskulptor.org/

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
global guess


# helper function to start and restart the game
def new_game():
    range100()


# define event handlers for control panel
def range100():
    global guess,r
    guess=7
    r=random.randrange(0,100)
    print ""
    print "New Game ,Range is from 0 to 100"
    print "Number of remaining guess is",guess

def range1000():
    global guess,r
    guess=10
    r=random.randrange(0,1000)
    print ""
    print "New Game ,Range is from 0 to 1000"
    print "Number of remaining guess is",guess
    
def input_guess(pguess):
    global guess
    print ""
    print "Guess was",pguess
    pguess=int(pguess)
    guess-=1
    print "Number of remaining guess is",guess
    if pguess < r:
        print "Higher"
    elif pguess >r:
        print "Lower"
    else:
        print "Correct"
        new_game()
    if guess==0:
        print ""
        print "Out of Guesses\nBad Luck\nBetter Luck Next Time"
        new_game()
    
# create frame
frame=simplegui.create_frame("Guess the Number",200,200)
frame.add_button("Range is (0,100)",range100,200)
frame.add_button("Range is (0,1000)",range1000,200)
frame.add_input("Enter a Guess",input_guess,50)
# register event handlers for control elements and start frame
frame.start

# call new_game
new_game()
# always remember to check your completed program against the grading rubric
