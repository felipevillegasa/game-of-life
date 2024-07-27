from flask import Flask, render_template, jsonify, request
from game import game_of_life
import numpy as np

app = Flask(__name__)
game = game_of_life(grid_size=20, start_alive=140) #20x20 grid with 30% cells alive

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/step', methods=['POST'])
def step():
    new_grid = game.update_grid()
    end_condition = game.detect_end_condition()
    response = {
        'grid': new_grid.tolist(),
        'end_condition': end_condition
    }
    return jsonify(response)

@app.route('/initialize', methods=['GET'])
def initialize():
    initial_grid = game.get_grid()
    return jsonify(initial_grid)

@app.route('/toggle', methods=['POST'])
def toggle():
    data = request.json
    row, col = data['row'], data['col']
    turn_on = data.get('turnOn', False)
    if turn_on:
        game.grid[row, col] = 1
    return jsonify(success=True)

@app.route('/clear', methods=['POST'])
def clear():
    game.grid = np.zeros_like(game.grid)
    return jsonify(success=True)

@app.route('/randomize', methods=['POST'])
def randomize():
    grid_size = game.grid_size
    num_alive = int(grid_size * grid_size * 0.3) #30% of the grid
    game.grid = np.zeros((grid_size, grid_size), dtype=int)
    alive_cells = np.random.choice(grid_size*grid_size, num_alive, replace=False)
    for cell in alive_cells:
        row = cell // grid_size
        col = cell % grid_size
        game.grid[row, col] = 1
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
