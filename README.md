# My battleship app
Battleships is an old strategic guessing game usually played by two players.  Each player places ships of different sizes on their own game board which is usually the size of a 10 by 10 grid. The objective of this game is to sink the opponents' ship by strategically guessing their coordinates. This  project  allows you to play by either yourself or versus an ai in through the command-line interface or the web. Below are some examples on how you can run the app.

## Prerequisites
Before running the Battleships game make sure you have the following installed:
	- Python 3 which you can install from python.org
	-  graphical user interface flask which you can install through the Python terminal using pip install Flask command
## Singleplayer
The singleplayer game mode is played by executing the function simple_game_loop() within the game_engine.py file. The game_engine.py file consists of four functions:
- attack: This function takes three arguments coordinates, board and battleships. It checks if there is a battleships at the coorrdinate on the board for the corresponding attack. The attack can be either a hit or miss, when it is a hit it updates coordinate position to a None value and decreases the size of the hit ship.
- cli_coordinate: This function takes no arguments and prompts the user to input to coordinates for an attack. 
- draw_board: This functions takes one arguments board and draws the board with battleships
- single_game_loop: This function takes no arguments and is meant for intermediate manual testing through the command line. 
When playing single_game_loop should run like this:
	1. Start the game with a welcome message.

	2. Initialise the board, the ships and place the ships using the default settings to 			  create the game components.

	3. Prompt the user to input coordinates of their attack.

	4. Process the attack on the single board created above. Print a hit or miss message 	to the user each time.

	5. Repeat steps 4 and 5 until all battleships have been sunken.

	6. Print game over message.

If the user inputs an invalid value (a non integer value) for either x or y coordinates a message 'You entered an invalid nummber.' is printed and the cli_coordinates functions is executed again. The program does not stop when encountering this value error.

## AI
We can play versus an AI opponent through the command-line interface or the web.
 
When playing through the terminal the player has to execute the ai_opponent game loop in the mp_game_engine.py . The mp_game_engine.py file has 3 functions: 
- generate_attack: This function represents the attack of an AI
- ai_opponent_game_loop: This function takes no arguments. It allows the user to play versus an AI opponent through the command-line interface.

The ai_opponent_game_loop should run like this:
1.  Start the game with a welcome message.
2.  Initialise two players in the dictionary, create their battleships and board. One player will be the user and the second player will be the AI opponent. Place the battleships using the random placement algorithm for the AI opponent and custom placement algorithm for the user. Remember, there should be a placement.json file that can be updated by the user player to configure their setup.
3.  Prompt the user to take their turn and input the coordinates of their attack.
4.  Process the attack on the board of the AI opponent player. Print a Hit or Miss message to the user each time.
5.  Generate an attack from the AI opponent against the user player and process the attack on the board of the user player. Print a Hit or Miss message to the user each time. When reporting the AI opponent Hit or Miss, include an ascii representation of the user player’s board after each turn.
6.  Repeat steps 3 to 5 until all battleships for one player have been sunken.
7.  Print appropriate game over message depending on whether the user won or lost.

If the user enters an invalid value or an integer that is bigger than the length of the board itself a message will be printed, prompting the user to enter another valid value. Another message, announcing the winner will be printed when either a player or the AI has won.

To play through the web the user has to run the main.py file, which prints out an url in the terminal. The user has to then enter the url in the browser and add /placement at the end.

## Testing
Before running tests you have install pytest which you can do by running pip install pytest in the terminal. Once you have done that you can run the tests by executing pytest command in the terminal.
