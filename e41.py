#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-20 20:49:14
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import sys
import random
from urllib.request import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {
"class %%%(%%%):":
 "Make a class named %%% that is-a %%%.",
 "class %%%(object):\n\tdef __init__(self, ***)" :
 "class %%% has-a __init__ that takes self and *** params.",
 "class %%%(object):\n\tdef ***(self, @@@)":
 "class %%% has-a function *** that takes self and @@@ rams.",
 "*** = %%%()":
 "Set *** to an instance of class %%%.",
 "***.***(@@@)":
 "From *** get the *** function, call it with params self, @.",
 "***.*** = '***'":
 "From *** get the *** attribute and set it to '***'."
 }

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

print(WORDS)

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(", ".join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


if __name__ == "__main__":
    try:
        while True:
            snippets = list(PHRASES.keys())
            random.shuffle(snippets)

            for snippet in snippets:
                phrase = PHRASES[snippet]
                question, answer = convert(snippet, phrase)
                if PHRASES_FIRST:
                    question, answer = answer, question
                print(question)

                input("> ")
                print(f"ANSWER: {answer}\n\n")
    except EOFError:
        print("\nBye")
