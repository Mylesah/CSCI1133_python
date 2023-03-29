
#==========================================
# Purpose: combines dictonaries 1 and 2 to return a combined dictionary where values of the smae key are added together, dSum
# Input Parameter(s): d1: the first dictionary, d2: the second dicitonary
# Return Value(s): dSum: the combined dictionary which has summed values for the keys that are in both dictionaries
#==========================================

def combine(d1, d2):
    dSum = {}
    summed = []
    for key, value in d1.items():
        if key in d2:
            summed.append((key, value + d2[key]))
        else:
            summed.append((key, value))
    for key, value in d2.items():
        if key not in d1:
            summed.append((key, value))
    dSum = dict(summed)
    return dSum


#==========================================
# Purpose: finds the first word of every sentance in a document and counts the number of times a sentance starts with that word
# Input Parameter(s): fname: the name of a txt file that will be used
# Return Value(s): fwords
#==========================================

def first_words(fname):
    fp = open(fname, 'r')
    text_list = []
    fwords = {}
    text_list = fp.readlines()
    nested_list = []
    for lines in text_list:
        b = lines.split()
        nested_list.append(b)
    for lists in nested_list:
        first = lists[0]
        if first not in fwords:
            fwords[first] = 1
        else:
            fwords[first] += 1
    fp.close()
    return fwords

#==========================================
# Purpose: a helper function for next_words, creates a nested dictionary using word and every string that is directley after every occurance of word in long_str
# Input Parameter(s): long_str: a list of one word strings
# Return Value(s): my_dict: a nested dictionary which uses the word as the key
# and the value is another dictionary where every word directley after word is a key and the value is the number of occurances in long_str
#==========================================

def helper_1(long_str, word):
    listed = []
    empty = []
    my_dict = {}
    listed.append(word)
    freq = long_str.count(word)
    start = 0
    for i in range(freq):
        idx = long_str.index(word, start) + 1
        listed.append(long_str[idx])
        start = idx
    key = listed[0]
    listed.pop(0)
    for j in listed:
        dict_entry = (j, listed.count(j))
        if dict_entry not in empty:
            empty.append((j, listed.count(j)))
    my_dict[key] = dict(empty)
    return(my_dict) #returns {'word', {'words': #, 'after':#, 'word': #}
        
#==========================================
# Purpose: calls helper_1 and uses the file, fname to return ndict, a nested dictionary
#where each key reffers to another dictionary which has every word after the original key as a key and has the number of occurances of that word in fname as the value
# Input Parameter(s): fname: the name of the file which the function is reading from
# Return Value(s): ndict, which is a nested dictionary 
#==========================================        

def next_words(fname):
    fp = open(fname, 'r')
    text_str = fp.read()
    text_str = text_str.split('\n')
    long_str = ''
    for string in text_str:
        long_str += string + ' '
    long_str = long_str.split(' ')
    short_str = []
    for i in long_str:
        if i not in short_str and i != '':
            short_str.append(i)
    ndict = {}
    for word in short_str:
        if word != '.':
            ndict.update(helper_1(long_str, word)) 
    fp.close()         
    return ndict

      
#==========================================
# Purpose: prints 10 strings that end in '.' by randomly selecting words from the keys in ndict and the strings in firstw_list
# Input Parameter(s): fname: the name of a text file that the function's call functions are reading from
# Return Value(s): 
#==========================================
import random

def fanfic(fname):
    firstw = first_words(fname)
    firstw_list = []
    for key, value in firstw.items():
        for i in range(value):
            firstw_list.append(key)
    ndict = next_words(fname)
    for j in range(10):
        empty = ''
        start = random.choice(firstw_list)
        empty = start + ' '
        nextw = random.choice(list(ndict[start].keys()))
        while nextw != '.':
            nextw = random.choice(list(ndict[nextw].keys()))
            empty += nextw + ' '
        print(empty)

        
