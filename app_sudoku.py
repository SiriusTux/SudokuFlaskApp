from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from utility import removeDot, grid_values
from sudoku import solve
from random import choice
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sudoku.db'
db = SQLAlchemy(app)

class Grid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grid = db.Column(db.String(81), nullable=False)
    difficulty = db.Column(db.String(10), nullable=False, default='Easy')
    source = db.Column(db.String(255), nullable=False, default='Unknown')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Grid({self.id}, {self.grid}, {self.source})'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        level = request.form['level']
        grid_list = Grid.query.filter(Grid.difficulty == level).all()
        grid= choice(grid_list)
        clean_grid = removeDot(grid_values(grid.grid))
        description = grid.source+', ' + \
            str(grid.date.day)+' '+str(grid.date.strftime("%B")) + \
            ' '+str(grid.date.year)
        return render_template('solve.html', description=description, id=grid.id, grid=clean_grid)
    nof_easy = Grid.query.filter(Grid.difficulty == 'Easy').count()
    nof_medium = Grid.query.filter(Grid.difficulty == 'Medium').count()
    nof_hard = Grid.query.filter(Grid.difficulty == 'Hard').count()
    difficulty_count = {'easy': nof_easy, 'medium': nof_medium, 'hard': nof_hard}
    empty_grid = removeDot(grid_values(
        '.................................................................................'))
    return render_template('start.html', grid=empty_grid, difficulty=difficulty_count)


@app.route('/solved/<int:grid_id>')
def solved(grid_id):
    to_solve = Grid.query.get(grid_id).grid
    solved = solve(to_solve)
    return render_template('solved.html', grid=solved)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

