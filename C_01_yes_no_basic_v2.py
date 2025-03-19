
# functions go here

def yes_no(question):

    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            print("you said no")
            break
        else:
            print("please enter yes / no")
            continue
def instructions():
    """Prints instructions"""

print("""       
***INSTRUCTIONS!***

ROLL THE DICE! TRY TO WIN!
    """)



# Main routine

# Ask the user if they want instructions (check they say yes / no)
Want_instructions = yes_no("do you want to see the instructions? ")
want_coffee = yes_no("do you want coffee? ")

print("we are done")

