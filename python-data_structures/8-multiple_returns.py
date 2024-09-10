#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:  # Si la phrase n'est pas vide
        return (len(sentence), sentence[0])
    else:  # Si la phrase est vide
        return (0, None)
