from flask import Flask, render_template, jsonify, request, app
from components import place_battleships, initialise_board, create_battleships
from game_engine import attack as attack1
from mp_game_engine import draw_board, generate_attack
import json


player_ships = create_battleships()
AI_ships = create_battleships()
initialised_player_board = []
AI_board = place_battleships(initialise_board(), AI_ships, algorithm = 'random')



app = Flask(__name__)

@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    global player_ships
    if request.method == 'GET':
        return render_template('placement.html', ships = player_ships, board_size = 10)
    if request.method == 'POST':
        data = request.get_json()
        a = json.dumps(data, indent = 4)
        with open('placement.json', 'w') as f:
            f.write(a)

        return jsonify({'message': 'Received'}),200



@app.route('/', methods = ['GET'])
def root():
    global initialised_player_board, player_ships
    initialised_player_board = place_battleships(initialise_board(), player_ships, algorithm='custom')
    if request.method == 'GET':
        return render_template('main.html', player_board=initialised_player_board)

@app.route('/attack', methods = ['GET'])
def process_attack():
    global AI_board, AI_ships, player_ships, initialised_player_board
    if request.method == 'GET' and request.args:
        winner = ''
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        x_AI,y_AI = generate_attack()
        player_hit = attack1((x,y), AI_board, AI_ships)
        AI_hit = attack1((x_AI, y_AI), initialised_player_board, player_ships)
        if AI_ships and player_ships:
            return jsonify({
                'hit': player_hit,
                'AI_Turn': (x_AI, y_AI)
            })
        else:
            if not AI_ships:
                winner = 'Player'
            else:
                winner = 'AI'

        return jsonify({'hit': player_hit,
                'AI_Turn': (x_AI,y_AI),
                'finished': 'Game Over ' + winner + ' wins'
                })
       
    
if __name__ == '__main__':
    app.run()

