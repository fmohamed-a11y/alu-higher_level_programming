#!/usr/bin/python3
def multiply_returns(sentence):
    if len(sentence) ==0:
        return (0, None)
    return (len(sentence), sentence[0])
