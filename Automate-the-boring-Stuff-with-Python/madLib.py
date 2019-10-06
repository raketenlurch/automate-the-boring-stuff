#!usr/bin/venv python3
"""
Create a Mad Libs programm that reads in text files and lets the user add
their own text anywhere where the word ADJECTIVE, NOUN, ADVERB or VERB
appears in the text file. The programm would find these occurrences and prompt the
user to replace them.
"""
import re

text = open("sentence.txt", "r+")

for word in text:
    matchingObject = re.match(r"ADJECTIVE|NOUN|ADVERB|VERB")
    if matchingObject == word:
