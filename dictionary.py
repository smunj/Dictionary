import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open("data.json"))


def get_meaning(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        inn = input("Did you mean %s? Enter Y if yes, N if no: " % get_close_matches(word, data.keys())[0])
        if inn == "Y" or inn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif inn == "N" or inn == "n":
            return "The word doesn't exist."
        else:
            return "Please start again"
    else:
        return "Word does not exist!"


word = input("Enter word: ")
out = get_meaning(word.lower())
if type(out) == list:
    for i in range(len(out)):
        print(str(i+1) + '. ' + out[i] )
else:
    print(out)


