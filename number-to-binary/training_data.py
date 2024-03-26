import random
data_i = {i,bin(i)[2:].rjust(4,'0')) for i in range(10)}
data = tuple(data_i.items())

def series(n):
    return (random.choice(data) for i in range(n))
