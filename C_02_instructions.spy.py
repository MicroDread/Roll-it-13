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


# Main routine
# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no(" do you want to see the instructions? ")

# display the instruction if the user wants to see them
if want_instructions == "yes":
        instructions()

print("program continues")
