"""
# ---------------------------------------------------
# Name : Ayra Qutub
# SID: 1708104
# CCID : aqutub
# AnonID : 1000316555
# CMPUT 274 , Fall 2022
#
# Weekly Exercise 3: Word Frequency
# ---------------------------------------------------

TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""
# Help received from TA: E. McDonald

import sys
# Global List
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now"
    ]


def split(input):
    input = input.split()
    return input


def lowercase(input):
    # convert word to lowercase
    List = []
    for i in input:
        low = i.lower()
        List.append(low)
    return List


def puncsymb(input):
    # remove punctuation and symbols
    List = []
    for char in input:
        string = ""
        for letter in char:
            if (letter.isalpha()) or (letter.isnumeric()):
                string += letter
        List.append(string)
    return(List)


def num(input):
    # remove numbers from words that don't consist only of numbers
    List = []
    for char in input:
        if char.isnumeric():
            # if entire word is numbers
            List.append(char)
        else:
            for letter in char:
                letters = list(char)
                if letter.isnumeric():
                    letters.remove(letter)
                    char = "".join(letters)
            List.append(char)
    return(List)


def stops(input):
    List = []
    for word in input:
        if word in Stop_Words:
            pass
        else:
            List.append(word)
    return (List)


def processed(input):
    List = []
    for word in input:
        if word is word:
            List.append(word)
    return(List)


def errorcheck(input):
    if input != "keep-digits" or "keep-stops" or "keep-symbols":
        Exception("Usage: preprocess.py keep-symbols|keep-stops|keep-digits")
        return(1)
        exit()


def output(input):
    output = ""
    out = processed(stops(num(puncsymb(lowercase(split(input))))))
    output = " ".join(out)
    output = output.rstrip()
    return(output)


def kdigs(input):
    output = ""
    out = processed(stops(puncsymb(lowercase(split(input)))))
    output = " ".join(out)
    output = output.rstrip()
    return(output)


def kstos(input):
    output = ""
    out = processed(num(puncsymb(lowercase(split(input)))))
    output = " ".join(out)
    output = output.rstrip()
    return(output)


def ksyms(input):
    output = ""
    out = processed(stops(num(lowercase(split(input)))))
    output = " ".join(out)
    output = output.rstrip()
    return(output)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.

    input = input()
    errorcheck(input)
    out = ""

    if len(sys.argv) < 2:
        out = output(input)
    elif sys.argv[1] == "keep-digits":
        out = kdigs(input)
    elif sys.argv[1] == "keep-stops":
        out = kstos(input)
    elif sys.argv[1] == "keep-symbols":
        out = ksyms(input)
    print(out)
