#!/usr/bin/python3

def multiple_returns(sentence):
    """
    @args - sentence string argument
    returns - tuple with length of string and first character
    """
    str_len, first_char = len(sentence), sentence[0]
    return (str_len, first_char)
