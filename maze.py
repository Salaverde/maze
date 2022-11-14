import readchar
import os
import random

POS_X = 0
POS_Y = 1

player_position = [1, 1]
tail_length = 0
player_tail = []

gold_distribution = []
total_coins = random.randint(10, 30)
end_game = False
died = False

# MAP DESIGN
object_distribution = """\
###   #####    #####
##      ###  #######
###      #     #####
##   ##     ########
###         ########
######            ##
#        ###########
####   #############
####         #######
###  #####    ######
##    ####       ###
###          #######
#     ###     ######
###   ######    ####
####################\
"""

object_distribution = [list(row) for row in object_distribution.split("\n")]
MAP_WIDTH = len(object_distribution[0])
MAP_HEIGHT = len(object_distribution)


# Main Loop
while not end_game:

    while len(gold_distribution) < total_coins:

        new_coin = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]

        if new_coin not in gold_distribution and new_coin != player_position and \
                object_distribution[new_coin[POS_Y]][new_coin[POS_X]] != "#":
            gold_distribution.append(new_coin)

    # DRAW MAP
    os.system("cls")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            # DRAW COINS
            for gold_coin in gold_distribution:
                if coordinate_y == gold_coin[POS_Y] and coordinate_x == gold_coin[POS_X]:
                    char_to_draw = "*"
                    object_in_cell = gold_coin

            # DRAW PLAYER HEAD AND TAIL
            for tail_piece in player_tail:
                if tail_piece[POS_Y] == coordinate_y and tail_piece[POS_X] == coordinate_x:
                    char_to_draw = "O"
                    if player_position in player_tail:
                        tail_in_cell = tail_piece
            if player_position[POS_Y] == coordinate_y and player_position[POS_X] == coordinate_x:
                char_to_draw = "0"

                # A COIN IS COLLECTED
                if object_in_cell:
                    gold_distribution.remove(object_in_cell)
                    tail_length += 1

            # PLAYER HITS TAIL
            if tail_in_cell:
                died = True
                end_game = True
                break
            # DRAW OBSTACLE
            if object_distribution[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("COINS COLLECTED: {}".format(tail_length))

    if died:
        break
    # Where does the player want to move?
    direction = readchar.readchar()
    new_position = None
    if direction == "w":
        new_position = [player_position[POS_X], (player_position[POS_Y] - 1) % MAP_HEIGHT]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_tail.insert(0, player_position.copy())
            player_tail = player_tail[:tail_length]
            player_position = new_position

    elif direction == "s":
        new_position = [player_position[POS_X], (player_position[POS_Y] + 1) % MAP_HEIGHT]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_tail.insert(0, player_position.copy())
            player_tail = player_tail[:tail_length]
            player_position = new_position


    elif direction == "a":
        new_position = [(player_position[POS_X] -1) % MAP_WIDTH, player_position[POS_Y]]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_tail.insert(0, player_position.copy())
            player_tail = player_tail[:tail_length]
            player_position = new_position


    elif direction == "d":
        new_position = [(player_position[POS_X] + 1) % MAP_WIDTH, player_position[POS_Y]]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_tail.insert(0, player_position.copy())
            player_tail = player_tail[:tail_length]
            player_position = new_position

    elif direction == "q":
        end_game = True


os.system("cls")
if died:
    print("YOU DIED!")
input("\nYOU COLLECTED {} COINS.".format(tail_length))

os.system("cls")

