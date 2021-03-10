# Python program for jumbled words game. 
# import random module 
import random 
# function for choosing random word. 
def choose():
    words=[]
    if not words:
        with open("jumblewords.txt","r") as list:
            for word in list:
                word=word.strip('\n')
                if (len(word)>4):
                    words.append(word)
    pick = random.choice(words)
    return pick 

# Function for shuffling the 
# characters of the chosen word. 
def jumble(word): 
	# sample() method shuffling the characters of the word 
	random_word = random.sample(word, len(word)) 
	jumbled = ' '.join(random_word) 
	return jumbled 

 
def jw(): 
	# variable for counting score. 
    scr = 0
	# keep looping 
    while True: 
		# choose() function calling 
        picked_word = choose() 
        # jumble() fucntion calling 
        qn = jumble(picked_word) 
        return qn
          

