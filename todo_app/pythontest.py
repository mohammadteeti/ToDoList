import random

def get_random(all_words):
    return random.choice(all_words)


all_words= "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt mollitia repellat, repudiandae qui a aliquid fuga quasi, numquam, officiis deserunt quas voluptate ab? Hic perspiciatis ad, repudiandae natus similique animi?".split()


uniqueWord=[]
for i in range (0,1001):
    word=get_random(all_words) 
    if not (word in uniqueWord):
        uniqueWord.append(word)
        
print(uniqueWord)


