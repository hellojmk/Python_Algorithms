# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"
sentence3 = "Hello! World! Hello! World! Hello! World! Hello! World! Hello! World! "

def averageLength(x):
    
    # For loop to remove puctuations
    for punctuation in ",.!":
        # Replace all the punctuations into ''
        x = x.replace(punctuation, '')
    
    # After removing all punctuations, split sentence into words
    words = x.split()
    # Get average length of sentence using lambda
    average = sum(len(word) for word in words) / len(words)
    
    return average

print(averageLength(sentence1))
print(averageLength(sentence2))
print(averageLength(sentence3))   