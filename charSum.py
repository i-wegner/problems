
alph = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

def dictCount(alph, string):

    string = string.lower()

    for (x, y) in alph.items():
        num = string.count(x)
        y += num
        alph.update({x: y})

    return alph

for (x, y) in alph.items():
    print(f"{x} : {y}")