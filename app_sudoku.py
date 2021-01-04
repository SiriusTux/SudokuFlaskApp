from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from utility import removeDot, grid_values
from werkzeug.security import check_password_hash
from gridForm import GridForm
from sudoku import solve
from random import choice
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sudoku.db'
app.config['SECRET_KEY'] = 'Mysecret!'
db = SQLAlchemy(app)
hashed_password = 'sha256$Y4HpS0CL$136c9b2c6fe7f8ff2778fcdea77e1a4e9bd4f0a6ce02c3e1c9de7e244b9d996b'
empty = '.................................................................................'

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
    empty_grid = removeDot(grid_values(empty))
    return render_template('start.html', grid=empty_grid, difficulty=difficulty_count)

@app.route('/solved/<int:grid_id>')
def solved(grid_id):
    to_solve = Grid.query.get(grid_id).grid
    solved = solve(to_solve)
    return render_template('solved.html', grid=solved)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user == 'admin' and check_password_hash(hashed_password, password):
            form = GridForm()
            return render_template('new.html', form=form)
        return render_template('login.html', error='Login Failed!')
    return render_template('login.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
    form = GridForm()
    if request.method == 'POST' and form.validate():
        new_grid = dict(request.form)
        del new_grid['csrf_token']
        return new_grid
    return render_template('new.html', form=form )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

