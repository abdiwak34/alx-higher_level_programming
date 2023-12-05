#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    lng = len(sentence)
    char = sentence[0]
    tup = (lng, char)
    return tup
