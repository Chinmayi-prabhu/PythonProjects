import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
            yn= input("Did you mean  %s instead? Enter Y if yes else N" % get_close_matches(word, data.keys())[0])
            yn= yn.upper()
            if yn =='Y':
                    return data[get_close_matches(word, data.keys())[0]]
            else:
                return 'the word does not exist please double check'             
    else:
        
        return 'the word does not exist please double check'


word= input('Enter the word you wnat to know meaning of : ')

output= translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)