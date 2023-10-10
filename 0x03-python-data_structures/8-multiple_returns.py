#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)  # Return (0, None) for an empty sentence
    else:
        return (len(sentence), sentence[0])  # Return length and first char
