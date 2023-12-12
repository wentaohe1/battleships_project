from components import initialise_board, create_battleships, place_battleships, check_row, check_column, board, ships


battleships = create_battleships('battleships.txt')
def attack(coordinates, board, battleships):
    '''
    This function takes three arguments coordinates, board and battleships. It checks if there is a battleships at the coorrdinate on the board for the corresponding attack. 
    The attack can be either a hit or miss, when it is a hit it updates coordinate position to a None value and decreases the size of the hit ship.
    :param coordinates: A tuple (x,y) representing a position on the board
    :param board: A list of lists representing the board state
    :param battleships: A dictionary with keys as battleship names and values as its sizes
    :return: True if its a hit and False if its a miss
    '''
    print(coordinates)
    (x,y) = coordinates
    
    for ship_name, ship_size in battleships.items(): #iterate through ships and their coordinates to check if they are there
        if board[x][y] == ship_name:
            print('Hit')
            board[x][y] = None
            battleships[ship_name] -= 1 #decrease the size of the ship
            if battleships[ship_name] == 0:
                print('You have sunk ' + ship_name + '!')
                battleships.pop(ship_name)
                
            
            return True
    else:
        print('Miss')
        return False


def cli_coordinates_input():
    '''
    This function takes no arguments and prompts the user to input to coordinates for an attack
    return: Coordinates represented by a tuple (x,y) 
    '''
    #prompt the user to enter coordinates in the command-line
    try:
        input_x_coordinates = int(input('Please enter the x coordiantes of your attack ( 0 - ' +str(len(board) - 1)+'): '))
        input_y_coordinates = int(input('Please enter the y coordiantes of your attack ( 0 - ' +str(len(board) - 1)+'): '))
    except ValueError:
        print('You entered an invalid number.')
        return cli_coordinates_input()
    if input_x_coordinates > int(len(board) - 1) or input_y_coordinates > int(len(board) - 1): #checks if x or y coordinates are bigger then the size of the row/column
        print('The number you\'ve enetered exceeds the maximum board size')
        return cli_coordinates_input()
    coordinates = (input_x_coordinates,input_y_coordinates)
    print('Your coordinates are:', coordinates)
    return coordinates

def draw_board(board):
    '''
    This functions takes one arguments board and draws the board with battleships
    '''
    print('-' * len(board) * 6) #the upper border of the board
    for row in board:
        print("|", end='') #the sides of the board
        for element in row: #placing the ships on the board
            if element:
                print(element, end='|')   #
            else:
                print(' ' * 5, end='|')
        print()
        print('-' * len(board) * 6) #the lower order of the board
   


def simple_game_loop():
    '''
    This function takes no arguments and is meant for intermediate manual testing through the command line.
    '''
    print('Welcome to the battleships game!') #starts with a welcome message
    board = initialise_board(10) #initialises the board
    ships = create_battleships('battleships.txt') 
    ship_placement = place_battleships(board, ships, algorithm='simple')
    while True:
        coordinates = cli_coordinates_input() #prompt the user to input coordinates of their attack
        print(draw_board(board))
        if coordinates is not None: #if there is a ship an attack is processed
            attack(coordinates, board, battleships)
        elif coordinates is None:
            print('Please try again.')
        else:
            print('You have sunk all ships. Game over. You win')
            break

if __name__ == '__main__':
    simple_game_loop()



        
        
        



