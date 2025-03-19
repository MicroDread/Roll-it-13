from C_01_yes_no_basic import (want_instructions)


#functions go here

def yes_no(question):
        """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

        while True:
                response = input(question).lower()

                # check the user says yes / no / y / n
                if response == "yes" or response == "y":
                        return "yes"
                elif response == "no" or response == "n":
                        return "no"
                else:
                        print("please enter yes / no")


def instructions():
        """prints instructions"""

        print("""
**** instructions! ****
        
ROLL THE DICE AND TRY TO WIN!!!
""")


def int_check():
        """checks user enter an integer more than / equal to 13"""

        error = "please enter an integer more than / equal  to 13."

        while True:
                try:
                        response = int(input("what is the game goal? "))

                        if game_goal < 13:
                                print(error)
                        else:

                                return response

                except ValueError:
                        print(error)


# Main routine
# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no(" do you want to see the instructions? ")

# display the instruction if the user wants to see them
if want_instructions == "yes":
        instructions()

print()
pgame_goal = int_check()
print(game_goal)