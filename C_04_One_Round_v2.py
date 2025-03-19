import random

from C_04_One_Round_v1 import double_user, user_points
from C_05_Statement_Generator import make_statement


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

# Work out who won...
if user_points > comp_points:
    winner = "User"
else:
    winner = "Computer"
round_feedback = f"The {winner} won"

# double user points if eligible
if winner == "user" and double_user == "yes":
    user_points = user_points * 2

# Output round results
(make_statement
(statement= "Round Results", decoration= "|"))
print(f"User Points: {user_points} | Computer Points: {comp_points}")
print(round_feedback)
print()