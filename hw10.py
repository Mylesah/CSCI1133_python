

#==========================================
# Purpose: calculates the scrabble value of a word
# Input Parameter(s): word: a string
# Return Value(s): 0 if nothing in string, otherwise the score of each letter concatinating in recursion
#==========================================
def scrabble_score(word):
    scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 
'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 
'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 
't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    if len(word) == 0:
        return 0
    else:
        return scores[word[0]] + scrabble_score(word[1:])
        

#==========================================
# Purpose: finds all integers that x is divisible by
# Input Parameter(s): x: an integer
# Return Value(s): gcd_help()
#==========================================
def gcd(x):
    return gcd_help(x, 0, [])
#==========================================
# Purpose: helper function to gcd by finding all integers that x is divisible by
# Input Parameter(s): x: an intiger, div: a number that x is being divided by, div_lst: an integer
# Return Value(s): div_list if div is >= to x other wise returns (recursion) gcd_help 
#==========================================
def gcd_help(x, div, div_lst):
    if not div <= x:
        return div_lst
    else:
        if x % (div+1) == 0:
            div_lst.append((div+1))
        div += 1
        return gcd_help(x, div, div_lst)
#==========================================
# Purpose: compares which values x and y are both divisible by and returns True if it's only '1' and false if they share multiple numbers they're divisible by
# Input Parameter(s): x: and intger, y: an integer
# Return Value(s): True or False
#==========================================        
def relatively_prime(x, y):
    x_lst = gcd(x)
    y_lst = gcd(y)
    comp = []
    for i in x_lst:
        if i in y_lst:
            comp.append(i)
    if max(comp) == 1:
        return True
    else:
        return False
                      
#==========================================
# Purpose: (What does the function do?)
# Input Parameter(s): (Each parameter by name and what it represents)
# Return Value(s): (What gets returned? Possibilities?)
#==========================================

def find_filepath(directory, filename):
    if filename not in directory:
        return False
    else:  
        return #recurssion




    
    
