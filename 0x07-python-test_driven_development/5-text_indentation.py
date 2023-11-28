#!/usr/bin/python3

"""prints a text with 2 new lines after each of these characters: ., ? and :."""

def text_indentation(text):
    """text must be a string, otherwise raise a TypeError.
    There should be no space at the beginning or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = 0
    while t < len(text) and text[t] == ' ':
        t += 1

        while t < len(text):
            print(text[t], end="")
            if text[t] == "\n" or text[t] in ".?:":
                if text[t] in ".?:":
                    print("\n")
                    t += 1
                    while t < len(text) and text[t] == ' ':
                        t += 1
                        continue
                    t += 1
