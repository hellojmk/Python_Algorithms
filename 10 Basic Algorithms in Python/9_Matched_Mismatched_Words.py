# Given two sentences, return 
# (1) an array that has the words that appear in one sentence and not the other 
# (2) and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def matchingWord(x, y):
    # set() : Used to create a set in python. 
    # The set in python takes one parameter. 
    # It is an optional parameter that contains values to be inserted into the set. 
    # The values in the parameter should be a b (string, tuple) or collection(set, dictionary), or an iterator object.
    set1 = set(x.split())
    set2 = set(y.split())
    
    # ^ : A.symmetric_difference(B)
    # & : A.intersection(B)
    return sorted(list(set1 ^ set2)), sorted(list(set1 & set2))

print(matchingWord(sentence1, sentence2))