#!/bin/env python3
def test(test_f, n):
    answer = bin(n)[2:].rjust(4,'0')
    result = test_f(n)
    return sum(result[i:i+1]==answer[i:i+1] or 0 for i in range(len(answer)))
