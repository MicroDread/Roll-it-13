from C_03_integer_checker import game_goal


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



# Main routine starts here
game_goal = int_check()
print(game_goal)
