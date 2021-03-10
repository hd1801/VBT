# Import the modules required 
import json 
from nltk.corpus import wordnet 
from difflib import get_close_matches 
# Loading data from json file ref
# in python dictionary 
data = json.load(open("words.json")) 
def getsynonyms(word):
    synonyms = []
  
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
    return synonyms
def findmeaning(w):
    syns=wordnet.synsets(w)
    print(syns)
    return syns[0].definition()

def getantonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            if l.antonyms(): 
                 antonyms.append(l.antonyms()[0].name())
    return antonyms
