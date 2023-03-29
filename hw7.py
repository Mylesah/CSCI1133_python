#==========================================
#Purpose: Encrypts message using the Baconian cypher method
# Input Parameter(s): message: string that you wanted encoded, encoding: the string values you want to use to represent the cypher
# Return Value(s): message
#==========================================

def encrypt(message, encoding):
    i = 0
    j = 5
    code_list = []
    for k in range(int(len(encoding)/5)):
        letter_codes = ''
        letter_codes = encoding[i:j]
        code_list.append(letter_codes)
        i += 5
        j += 5
    #print(code_list)
    message = message.strip().lower()
    message = message.replace(' ', '')
    coded = ''
    y = 0
    for y in range(len(message)):
        if message[y].isalpha() == True:
            message_value = int(ord(message[y]) - ord('a'))#message value is working
            coded = coded + code_list[message_value]
    message = coded
    return message

#==========================================
#Purpose: Decrypts an encrypted message
# Input Parameter(s): message: an encrypted message, encoding: the encryption method that will be used to decode
# Return Value(s): message
#==========================================

def decrypt(message, encoding):
    i = 0
    j = 5
    code_list = []
    for k in range(int(len(encoding)/5)):
        letter_codes = ''
        letter_codes = encoding[i:j]
        code_list.append(letter_codes)
        i += 5
        j += 5
    a_z = []
    w = 92
    for w in range(len(code_list)):
        a_z.append(chr(ord('a')+ w))
        w += 1
    #print(a_z)
    message_list = []
    y = 0
    z = 5
    for m in range(int(len(message)/5)):
        message_codes = ''
        message_codes = message[y:z]
        message_list.append(message_codes)
        y += 5
        z += 5
    #print(message_list)
    f = 0
    final = ''
    for f in range(len(message_list)):
        g = 0
        for g in range(len(code_list)):
            if message_list[f] == code_list[g]:
                final = final + a_z[g]
            g += 1
        f += 1
    message = final
    return message

#==========================================
#Purpose: finds the longest common substring between two DNA sequences
# Input Parameter(s): first: the first DNA sequence, second: the second DNA sequence
# Return Value(s): longest
#==========================================

def longest_common(first, second):
    string_comparison = []
    i = 0
    for i in range(len(first)):
        j = 0
        for j in range(len(first)):
            if first[i:j] in second:
                if first[i:j] not in string_comparison:
                    string_comparison.append(first[i:j])
            j += 1
        i += 1
    longest = ''
    length = 0
    for m in range(len(string_comparison)):
        if len(string_comparison[m]) >= length:
            length = len(string_comparison[m])
            longest = string_comparison[m]
    return longest
                    
#==========================================
# Purpose: returns the index value of the first vowel or returns 'constants' if string has no vowels
# Input Parameter(s): word: a string
# Return Value(s): word.index[i] (which is the index value of the first vowel), or returns 'constants' if word contains no vowels
#==========================================

def vowel_index(word): #helper function finds the vowel index
    vowels = ['a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    listed = []
    for j in word: #check if word has no vowels
        if j not in vowels:
            listed.append(j)
    if len(listed) < len(word): #compares to make sure there are vowels in the word
        for i in word:            
            if i in vowels:
                return word.index(i)
    else:
        return 'constants'
    
#==========================================
# Purpose: turns a string into pig latin format
# Input Parameter(s): word: a string
# Return Value(s): word_1, word_2, or word_3
#==========================================

def translate(word): #helper function turns a word in piglatin
    vowel = vowel_index(word)
    if vowel == 'constants': #the word is all constants
        word_1 = word + 'ay'
        return(word_1)
    elif vowel > 0: #this words starts with a constant(s)
        constants = word[0:vowel]
        word_2 = word.replace(constants, '', 1)
        word_2 = word_2 + constants + 'ay'
        return(word_2)
    else:    #this word starts with a vowel
        word_3 = word + 'way'
        return(word_3)
    
#==========================================
# Purpose: finds string capitalization and punctuation and mutates the string to remove and then add it back after calling the translate function
# Input Parameter(s): word: a string
# Return Value(s): word
#==========================================

def caps_and_punc(word): #helper function modifys a pig latin word by looking for case and punctuation
    punctuation = ''
    for char in word:
        if ord(char) < 65: #runs if it is punctuation
            punctuation = char
            fix = word.replace(char, '')
        else: #not punctuation
            fix = word         
    loworup = ord(fix[0])#find if there's uppercase letters, using variable fix because confusing with calling ir word too many times
    if loworup <= 90 and loworup >= 65:
        word = translate(fix)
        word = word.capitalize()
    elif loworup <= 122 and loworup >= 97:
        word = translate(fix)
    word += punctuation
    return word

#==========================================
#Purpose: translates a prhase into pig latin
# Input Parameter(s): phrase: a string phrase
# Return Value(s): latin
#==========================================
def igpay(phrase):
    final_list = []
    phrase_list = phrase.split()
    for words in phrase_list:
        final_list.append(caps_and_punc(words))
    latin = ' '.join(final_list)
    return latin

