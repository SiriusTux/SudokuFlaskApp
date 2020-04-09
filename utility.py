
def removeDot(dict):
    for el in dict:
        if dict[el] == '.':
            dict[el] = '' 
    return dict