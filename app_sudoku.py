from flask import Flask, render_template, session
from utility import removeDot
from sudoku import solve, grid_values
from random import randrange

app = Flask(__name__)

grid_list = ['..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..',
            '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......',
            '2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3',
            '38..........4..785..9.2.3...6..9....8..3.2..9....4..7...1.7.5..495..6..........92',
            '2..94.1.5.6.7...9.....65..8..6.2.....2.....3.....7.6..9..65.....3...1.7.1.5.37..6',
            '24..83.7.....2....8..96..3.6......53..3...7..19......2.3..16..7....4.....8.53..19',
            '3..5...2.........3..........1...5...2...3...6...1...7..........5.........6...4..2',
            '16...43.7...1....43...87...6.24.9.7...9...4...3.7.52.6...36...57....1...8.35...61',
            '....67..........86.29....4...7.9.8......3...7..1..2.9..1...9..2...6..35.37.8.....',
            '3..4..6..7...9...38..3......3.521..........9..2..3..4..48..2.....6...1.......74..',
            '.5...8.2.4.3...7.1....5....1...4......9.7.6......2...8....3....2.6...9.5.7.1...4.',
            '..8.7....36.9....1.9.1.83...7.......28.....57.......2...37.2.9.4....1.38....9.1..'
            ]

@app.route('/')
def home():
    grid_id = randrange(len(grid_list))
    grid = grid_list[grid_id]
    clean_grid = removeDot(grid_values(grid))
    return render_template('start.html', id=grid_id, **clean_grid)


@app.route('/solved/<int:grid_id>')
def solved(grid_id):
    grid = grid_list[grid_id]
    solved = solve(grid)
    return render_template('solved.html', **solved)

if __name__ == '__main__':
    app.run(port=5000, debug=True)