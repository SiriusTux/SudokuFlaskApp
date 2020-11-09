from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from utility import removeDot, grid_values
from sudoku import solve
from random import randint
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


@app.route('/')
def home():
    grid_list = Grid.query.all()
    grid_id = randint(1, len(grid_list))
    grid = Grid.query.get(grid_id).grid
    clean_grid = removeDot(grid_values(grid))
    return render_template('start.html', id=grid_id, **clean_grid)


@app.route('/solved/<int:grid_id>')
def solved(grid_id):
    to_solve = Grid.query.get(grid_id).grid
    solved = solve(to_solve)
    return render_template('solved.html', **solved)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
