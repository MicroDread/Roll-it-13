import random

from C_04_One_Round_v1 import double_user, user_points
from C_05_Statement_Generator import make_statement


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


def initial_points(which_player):
    """Roll dice twice and return total / if devote points apply"""

    double = "no"

    #Roll the dice for the user Land note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(F"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double

def make_statement(statement, decoration):
#   """Adds emoji / additional characters

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

# Main starts here...

# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0
rounds_played = 0

game_history = []

make_statement(statement="Welcome to the Roll it 13 Game", decoration="🍀" )

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no(" do you want to see the instructions? ")

# display the instruction if the user wants to see them
if want_instructions == "yes":
        instructions()

print()
game_goal = int_check()

# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:
    rounds_played +=1

    # Start of round loop
    make_statement(statement= f"Round {rounds_played}", decoration= "🎲")

    # For testing purposes, ask the user what the points for the user / computer were
    # Roll the dice for the user and note if they
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    print("Initial User", initial_user)

    print("initial Computer", initial_comp)

    # Retrieve user points (first item from function)
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # Let the user know if they quality for double points
    # if double_user == "yes":
    #      print(" Good news! - if you win this round, you will earn Double points")

    # assume user goes first...
    First = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points, they start the game
    if user_points == comp_points:
        print("you start because your initial roll was less than the computer\n")

    # if user and computer roll = points, the user is player 1...
    elif user_points == comp_points:
        print("the initial rolls were the same, the"
              ""
              " user starts!")

    # if the computer has fewer points, switch the computer to 'player 1 else:
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, "first"

    # Loop until we have a winner...
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")

        # first person rolls the die and the score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points = player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person's score is over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the dice (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print("{second): Rolled a (player_2_roll) has player 2_points) points")

        print("{first): (player_1_points) (second) (player_2_points)")

    print("end Of Round")

    # associate player points with either the user or the computer
    user_points = player_1_points
    comp_points = player_2_points

    # Switch the user and computer points if the computer went first
    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # Work out who won and set the loser's points to zero
    if user_points > comp_points:
        winner = "User"
        loser = "computer"
        comp_points = 0
    else:
        winner = "Computer"
        loser = "user"
        user_points = 0
    round_feedback = f"The {winner} won.    The {loser}'s points have been reset to zero"

    # double user points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # Output round results
    make_statement( "Round Results",  "=" )
    print(f"user Points: {user_points} | Computer points: {comp_points}")

    # Outside rounds loop - Update score with round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_points

    # Generate round results and add it to the game history list
    game_results = (f"Round {rounds_played}: User Points {user_points} | "
                    f"Computer Points {comp_points}, {winner} wins "
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***")    # replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score {comp_score}")


# end of entire game output final results

make_statement(statement="Game Over", decoration="")

print()
if user_score > comp_score:
    make_statement(statement="The user won", decoration="🤙")   # replace this statement generator call
else:
    make_statement(statement="The computer won", decoration="💻")

print()
make_statement(statement="Game History", decoration="🎲")

for item in game_history:
    print(item)

