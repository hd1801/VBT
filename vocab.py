from vocabulary.vocabulary import Vocabulary as vb

def getdefine(word):
    return vb.meaning(word, format ="list")

def getsimilar(word):
    return  vb.synonym(word ,format ="list")   

def getopposite(word):
     return vb.antonym(word , format ="list")
    

def getusageexample(word):
    return vb.usage_example(word, format ="list")
    
def getpronunciation(word):
    return vb.pronunciation(word ,format ="list")
print(getusageexample("impact")[0])