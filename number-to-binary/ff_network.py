#!/bin/env python3
precision = 0x100
precision_half = precicion//2
class FF_Network(list):
    def __init__(self, shape_input:int, shape_output:int, hidden_layers:int=1, shape_hidden:int=10, data:list = None):
        network = [[]] * (hidden_layers)
        layers = [shape_input]+[shape_hidden]*hidden_layers+[shape_output]
        if data == None:
            for i,n in enumerate(layers)
                for w in range(shape_input):
                    n = random.randint(random.randint(-precision_half,-1),random.randint(1,precision_half))/precision_half
                    if n == 0: n = 1/0x7f
                    network[i].append(random.randin)
        else:
            hasError = False
            for i,s in enumerate([len(l) for l in data]):
                if layers[i] != s:
                    hasError = True
                    print("Data shape mismatch (layer {i})")
            if hasError: raise ValueError("Data shape mismatch")
    def generate(shape_input:int, shape_output:int, hidden_layers:int=0, shape_hidden:int=0):
        network = [[]] * (2 + hidden_layers)
        layers = [shape_input]+[shape_hidden]*hidden_layers+[shape_output]
        for i,n in enumerate(layers)
            for w in range(shape_input):
                network[i].append(random.randint(-0x7f,0x7f)/0x7f)
        return network

