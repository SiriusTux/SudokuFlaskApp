from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import AnyOf

class GridForm(FlaskForm):

    allowed_val = [str(x) for x in range(1, 10)]+['']

    A1 = StringField('A1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A2 = StringField('A2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A3 = StringField('A3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A4 = StringField('A4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A5 = StringField('A5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A6 = StringField('A6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A7 = StringField('A7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A8 = StringField('A8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    A9 = StringField('A9', validators = [AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    B1 = StringField('B1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B2 = StringField('B2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B3 = StringField('B3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B4 = StringField('B4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B5 = StringField('B5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B6 = StringField('B6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B7 = StringField('B7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B8 = StringField('B8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    B9 = StringField('B9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    C1 = StringField('C1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C2 = StringField('C2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C3 = StringField('C3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C4 = StringField('C4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C5 = StringField('C5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C6 = StringField('C6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C7 = StringField('C7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C8 = StringField('C8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    C9 = StringField('C9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    D1 = StringField('D1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D2 = StringField('D2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D3 = StringField('D3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D4 = StringField('D4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D5 = StringField('D5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D6 = StringField('D6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D7 = StringField('D7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D8 = StringField('D8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    D9 = StringField('D9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    E1 = StringField('E1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E2 = StringField('E2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E3 = StringField('E3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E4 = StringField('E4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E5 = StringField('E5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E6 = StringField('E6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E7 = StringField('E7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E8 = StringField('E8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    E9 = StringField('E9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    F1 = StringField('F1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F2 = StringField('F2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F3 = StringField('F3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F4 = StringField('F4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F5 = StringField('F5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F6 = StringField('F6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F7 = StringField('F7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F8 = StringField('F8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    F9 = StringField('F9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    G1 = StringField('G1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G2 = StringField('G2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G3 = StringField('G3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G4 = StringField('G4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G5 = StringField('G5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G6 = StringField('G6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G7 = StringField('G7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G8 = StringField('G8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    G9 = StringField('G9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    H1 = StringField('H1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H2 = StringField('H2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H3 = StringField('H3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H4 = StringField('H4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H5 = StringField('H5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H6 = StringField('H6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H7 = StringField('H7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H8 = StringField('H8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    H9 = StringField('H9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])

    I1 = StringField('I1', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I2 = StringField('I2', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I3 = StringField('I3', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I4 = StringField('I4', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I5 = StringField('I5', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I6 = StringField('I6', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I7 = StringField('I7', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I8 = StringField('I8', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
    I9 = StringField('I9', validators=[AnyOf(
        values=allowed_val, message='must insert a number from 1 to 9')])
