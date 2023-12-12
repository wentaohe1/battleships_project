
import random
import json
def initialise_board(size = 10):
    ''' 
    This function takes a number and returns a list of lists based on that number
    :param size: This is the size of the board, its default value is 10
    :return: A list of lists representing the board state
    '''
    board =  [[ None ] * size for x in range(size)]
    return board


def create_battleships(filename = 'battleships.txt'):
    '''
    This funtion takes one optional argument, filename with a default vallue of battleships txt. It reads the file and creates a dictionary with keys representin the battleship names and values representing their sizes
    :param filename: File containg the battleship names and its sizes.
    :return: A dictionary with battleship names and its sizes
    '''
    with open(filename, 'r') as lines:
        battleships = {}
        for line in lines:
            name, size = line.strip().split(':')
            battleships[name] = int(size)
    return battleships

#variable ships that represents the dictionary returned from the create_battleships function
ships = create_battleships('battleships.txt')
#variable board that represents the board state
board = initialise_board(10)

def place_battleships(board, ships, algorithm = 'simple'):
    '''
    This function takes three arguments: board, ships and algorithm with a default value of simple. It updates the board data structure to position the ships on the board.
    :param board: A list of lists representing the board state
    :param ships: A dictionary with keys as battleship names and values as its sizes
    :param algorith: Tells us how the ships are positioned on the board e.g. 'simple', 'random', 'custom'
    :return: A board with updated ship positions based on the algorithm and their size.
    '''
    def simple_algorithm(size, ship_name, board):
        '''
        This function positions the ships on the board based on the simple algorithm, i.e. each ship is placed horizontally on new rows starting from (0,0)
        :param size: The size of each battleships
        :param ship_name: The names of each battleship
        :param board: A list of lists representing the board state
        :return: A board where each ship is placed horizontally on new rows starting from (0,0)
        '''
        for i in range(size):
            board[row][i] = ship_name
    def random_algorithm(size, ship_name, board):
        '''
        This function positions the ships on the board based on the simple algorithm, i.e. each battleship is placed in random positions and orientations
        :param size: The size of each battleships
        :param ship_name: The names of each battleship
        :param board: A list of lists representing the board state
        :return: A board where each ship is placed on random positions either horizontally or vertically
        '''
        orientations = ['horizontally', 'vertically']
        orientation = orientations[random.randint(0,1)] #chooses a random orientation, either horizontal or vertical
        row = random.randint(0, len(board) - 1 -size) #chooses a random row where the battleship will be placed
        column = random.randint(0, len(board) - 1 - size) #chooses a random column where the battleship will be placed
        if orientation == "horizontally":
            row = random.randint(0, len(board) - 1 - size)
            column = random.randint(0, len(board) - 1 - size)
            a = check_row(board[row],size) 
            if not a: #If its false it chooses a new row and column with recursion
                random_algorithm(size, ship_name, board)
            elif any(board[i][column] is not None for i in range(row, row + size)):
                random_algorithm(size, ship_name, board)
            else:
                for i in range(column, column + size):
                    board[row][i] = ship_name
        else: #if orienrtation is vertical
            row = random.randint(0, len(board) - 1 - size)
            column = random.randint(0, len(board) - 1 - size)
            a = check_column([board[i][column] for i in range(len(board))], size)
            if not a:
                random_algorithm(size, ship_name, board)
            elif any(board[i][column] is not None for i in range(row, row + size)):
                random_algorithm(size, ship_name, board)
            else:
                for i in range(row, row + size):
                    board[i][column] = ship_name
    def custom_algorithm(size, ship_name, board):
        '''
        This function positions the ships on the board based on the simple algorithm, i.e. each battleship is placed where the user wants them to be
        :param size: The size of each battleships
        :param ship_name: The names of each battleship
        :param board: A list of lists representing the board state
        :return: A board where each ship is placed according to the placement configuration file, placement.json
        '''
        with open('placement.json') as placement_file: #reads the json file and turns it into a dictionary
            placement_dict = json.load(placement_file)
        for sn,values in placement_dict.items(): 
                if sn == ship_name:
                    x_coordinate = int(values[1])
                    y_coordinate = int(values[0])
                    orientation = values[2]
                    if orientation == 'h':
                        if int(y_coordinate) + size > len(board):  #prints and error if the ships is too big to be placed on a particular coordinate
                            print('Error. The ship {ship_name} is too big to be placed on {x_coordiante}, {y_coordinate} (size {size} orientation {orientation}).')
                        else:
                            for i in range(int(y_coordinate), int(y_coordinate) + size):
                                board[int(x_coordinate)][i] = sn
                    else:
                        if int(x_coordinate) + size > len(board):
                            print('Error. The ship {ship_name} is too big to be placed on {x_coordiante}, {y_coordinate} (size {size} orientation {orientation}).')
                        else:
                            for i in range(int(x_coordinate), int(x_coordinate) + size):
                                board[i][int(y_coordinate)] = sn
                                

    if algorithm == 'simple': #based on the algorithm it places the ships on each row 
        row = 0
        for ship_name, size in ships.items():
            simple_algorithm(size, ship_name, board)
            row += 1
    elif algorithm == 'random':
        for ship_name, size in ships.items():
            random_algorithm(size, ship_name, board)
    else:
        for ship_name, size in ships.items():
            custom_algorithm(size, ship_name, board)
    return board

def check_row(row, size):
    '''
    This function take two arguments row and size and checks if a battleship can be placed on a particular row
    :param row: Row of the board
    :param size: The size of the battleship
    :return: True if the ship can be placed on the particular row and False if it cannot be placed there
    '''
    count = 0
    minindex = 0
    maxindex = 0
    for i, space in enumerate(row):
        if space is None: #checks if a space is available for the ship to be placed and adds 1 to the count
            count += 1
        else:
            if count >= size: #if the count is bigger than size it means the ship can be placed on that row
                maxindex = i - 1
                minindex = i - count
                break
            else:
                count = 0
    if minindex == maxindex:
        if count > size:
            return [0, count]
        else:
            return False
    else:
        return [minindex, maxindex]

def check_column(column, size):
    return check_row(column, size)

