from components import initialise_board, create_battleships, place_battleships, board, ships
from game_engine import attack, cli_coordinates_input
import random 
players = {} #A dictionary that stores the name of each player as the key and their board and battleships as value

def generate_attack():
    '''
    This function represents the attack of an AI
    :return: A tuple with coordinates
    '''
    x = random.randint(0, len(board) - 1)
    y = random.randint(0, len(board) - 1)
    return (x,y)




def ai_opponent_game_loop():
    '''
    This function takes no arguments. It allows the user to play versus an AI opponent through the command-line interface.
    '''
    print('Welcome to the battleships game!')  #welcome message
    #ask for player username and board size
    player_username = input('Please enter your username:')
    #Player settings:
    initial_board_player = initialise_board()
    ships_player = create_battleships('battleships.txt')
    placement_settings_player = place_battleships(initial_board_player, ships_player, algorithm = 'custom')
    players[player_username] = [placement_settings_player, ships_player]
    #AI settings
    initial_board_AI = initialise_board()
    ships_AI = create_battleships('battleships.txt')
    placement_settings_AI = place_battleships(initial_board_AI, ships_AI, algorithm = 'random')
    players['AI'] = [placement_settings_AI, ships_AI]
    while ships_player and ships_AI: #if the player and AI still have battleships
        draw_board(placement_settings_player)
        attack(cli_coordinates_input(), placement_settings_AI, ships_AI)
        x,y = generate_attack()
        print("AI's result: ", x,y)
        attack((x,y), placement_settings_player, ships_player)
        if  all(count == 0 for count in ships_player.values()):
            print('AI has won. The game is now over.')
            break
        elif all(count == 0 for count in ships_AI.values()):
            print('User ', player_username, ' has won. The game is now over.')
            break

def draw_board(board):
    print('-' * len(board) * 6)
    for row in board:
        print("|", end='')
        for element in row:
            if element:
                print(element, end='|')   #'Ship' + str(i) to sm dou stran iz printa ker pol mi narobe imena ladij printa?
            else:
                print(' ' * 5, end='|')
        print()
        print('-' * len(board) * 6)

ai_opponent_game_loop()
   



        

