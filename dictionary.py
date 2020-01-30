import time
import json
from difflib import get_close_matches
dictionary = json.load(open("data/data.json"))

def extract_meaning(word):
    
    try:
        return dictionary[word]
    except KeyError:
        lower_word = word.lower()
        try:
            return dictionary[lower_word]
        except KeyError:
            try:
                return dictionary[lower_word.title()]
            except KeyError:
                try:
                    return dictionary[lower_word.upper()]
                except KeyError:
                    close_matches = get_close_matches(lower_word,dictionary.keys())
                    if len(close_matches) == 0:
                        return ["Sorry, the word doesn't exist."]
                    for each in close_matches:
                        choice = input("Did you mean %s ? Type y for yes or n for no: " % each)
                        if choice == "y":
                            return dictionary[each]
                    return ["Sorry, the word doesn't exist."]
start_time = time.time()        
if __name__ == "__main__":
    word = input("Enter a word to search in the dictionary: ")
    output = extract_meaning(word)
    #print(output)
    for each in output:
        print(each)
print("--- %s seconds ---" % (time.time() - start_time))