import requests
import json
from fetch_def import get_meaning
from fetch_def import get_wordtype
from fetch_def import get_prononciation
from fetch_def import get_WoD
def storeword(w):
    dictionary={
            "word": w,
            "meaning": get_meaning(w),
            "type": get_wordtype(w),
            "prononciation": get_prononciation(w)
            }
    print(dictionary)
    flag=0
    json_object=json.dumps(dictionary,indent=4)
    outfile=open("dailywordlist.json")
    data=json.load(outfile)
    for words in data:
        if(words==dictionary["word"]):
            flag=1
            break
    outfile.close()
    if(flag==0):    
        with open('dailywordlist.json', 'a') as outfile:
            outfile.write(json_object)

w=get_WoD()
storeword(w)
