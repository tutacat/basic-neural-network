import random
chars = "01"
def run(input):
    return chars[input & 8 > 0] + chars[input & 4 > 0] + chars[input & 2 > 0] + chars[input & 1]

def test():
    n = random.randint(0,9)
    return (n,run(n))

def __main__():
    for i in range(40):
        print(test())


if __name__ == '__main__':
    __main__()
