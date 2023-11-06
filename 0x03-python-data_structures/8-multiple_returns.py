#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    the_char = sentence[0] if length > 0 else "None"
    tuple_sen = length, the_char
    return(tuple_sen)
