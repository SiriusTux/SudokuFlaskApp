def cross(A, B):
    return [a + b for a in A for b in B]


def grid_values(grid):
    # Trasforma una grid in un dict {square : char}
    # dove char è un digits oppure '.' o '0'
    # se non è definito se il square deve essere vuoto
    # Se trovo altri caratteri in grid es. '|' li elimino
    chars = [c for c in grid if c in digits or c in '0.']
    # Alla fine voglio 81 caratteri, uno per ogni square
    assert len(chars) == 81
    return dict(zip(squares, chars))


def removeDot(dict):
    # Rimuove i punti
    for el in dict:
        if dict[el] == '.':
            dict[el] = ''
    return dict


digits = '123456789'
rows = 'ABCDEFGHI'
digits = '123456789'
cols = digits
squares = cross(rows, cols)
