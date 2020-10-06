##Ashleigh Schaible
##Project 2
##This is my own original work

import random

'''
This promptUserThrow() function uses input() to prompt the user to enter "R", "P", or "S" in order to throw "Rock", "Paper", or "Scissors", respectively.
This "R", "P", or "S" input is then stored as a string inside the local variable userThrow which then gets returned by the function.
'''
def promptUserThrow():
    userThrow = input("Let's play Rock Paper Scissors. \nEnter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. \n\nEnter your throw here --> ")
    return userThrow

'''
This function takes the returned value from the promptUserThrow() function and checks to see if it is equivalent to any of the valid expected inputs.
It then assigns to the variable checkError a boolean representing whether or not the user caused an error by entering a valid input or not, then returns this variable.
'''
def checkForError(userThrow): 
    validUserThrow = ["R", "P", "S"]
    if userThrow in validUserThrow:
        checkError = False;
    else:
        checkError = True;
    return checkError

'''
This function randomly chooses a valid throw for the computer using the random module and assigns it to a variable, then returns it.
'''
def computerThrows():
    validComputerThrows = ["R", "P", "S"]
    computerThrow = random.choice(validComputerThrows)
    return computerThrow

'''
This function takes the parameters userThrow and computerThrow, and assigns a numerical value to a new variable representing the winner based on the rules of Rock, Paper Scissors and the
parameters that represent the throws made by the user and the computer that are playing against each other. This numerical value representing the winner is then returned by the function.
A returned value equivalent to 0 represents a tie, 1 represents the user winning, and -1 represents the computer winning.
'''
def determineWinner(userThrow, computerThrow):
    if userThrow == computerThrow:
        winnerValue = 0; #tie
    elif userThrow == "P" and computerThrow == "R":
        winnerValue = 1; #user win
    elif userThrow == "R" and computerThrow == "S":
        winnerValue = 1; #user win
    elif userThrow == "S" and computerThrow == "P":
        winnerValue = 1; #user win
    else:
        winnerValue = -1; #computer win
    return winnerValue

'''
Main calls all of the other methods and stores values that pass between other functions. Within it is an if statement that determines whether or not to proceed after the user inputs
their throw, depending on whether or not the checkError() function determined the user input was valid. If it was invalid, it quits the program; if it was valid, it proceeds to call
the remaining functions through another if statement nested within it. It also ends the program if there is a keyboard interrupt. Lastly, it takes the winnerValue returned from
determineWinner(), and prints who won the game to the console as a string.
'''
def main():
    try:
        userThrow = promptUserThrow();
        checkError = checkForError(userThrow);
        if checkError == True:
            print("\n\nYou entered an invalid input. Please try again and enter a capital 'R', 'P', or 'S' to make your throw.")
        elif checkError == False:
            computerThrow = computerThrows();
            winnerValue = determineWinner(userThrow, computerThrow);
            if winnerValue == 0:
                print("\n\nYou tied with the computer!\nYou threw " + userThrow + " and the computer threw " + computerThrow + "!", sep="");
            elif winnerValue == 1:
                print("\n\nYou won against the computer!\nYou threw " + userThrow + " and the computer threw " + computerThrow + "!", sep="");
            elif winnerValue == -1:
                print("\n\nYou lost against the computer!\nYou threw " + userThrow + " and the computer threw " + computerThrow + ". Better luck next time!", sep="");
    except KeyboardInterrupt:
        print("\n\nKeyboard interrupted.\nPlease try again by restarting and only typing 'R', 'P', or 'S', and then hit 'enter'.")
        
main()

## -------------------------------------------------------
## Examples of input and output:


## -------------------------------------------------------
## Example 1: Inputted "R"
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> R
##
##
##You tied with the computer!
##You threw R and the computer threw R!


## -------------------------------------------------------
## Example 2: Inputted "P"
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> P
##
##
##You lost against the computer!
##You threw P and the computer threw S. Better luck next time!


## -------------------------------------------------------
## Example 3: Inputted "S"
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> S
##
##
##You won against the computer!
##You threw S and the computer threw P!


## -------------------------------------------------------
## Example 4: Inputted "r"
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> r
##
##
##You entered an invalid input. Please try again and enter a capital 'R', 'P', or 'S' to make your throw.


## -------------------------------------------------------
## Example 5: Inputted "p"
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> p
##
##
##You entered an invalid input. Please try again and enter a capital 'R', 'P', or 'S' to make your throw.


## -------------------------------------------------------
## Example 5: Inputted "8"
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> 8
##
##
##You entered an invalid input. Please try again and enter a capital 'R', 'P', or 'S' to make your throw.


## -------------------------------------------------------
## Example 7: ctrl-c was pressed.
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> 
##Keyboard interrupted. Please try again by restarting and only typing 'R', 'P', or 'S', and then hit 'enter'.


## -------------------------------------------------------
## Example 8: Inputted "hello"
##Let's play Rock Paper Scissors. 
##Enter 'R' for Rock; 'P' for Paper, or 'S' for Scissors. 
##
##Enter your throw here --> Hello
##
##
##You entered an invalid input. Please try again and enter a capital 'R', 'P', or 'S' to make your throw.

