#==========================================
# Purpose: Print 121 lines of "Who needs loops?"
# Input Parameter(s): (Each parameter by name and what it represents)
# Return Value(s): None
#==========================================

def func_1():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")    
def func_2():
    func_1()
    func_1()
    func_1()
    func_1()
    func_1()
def print_121():
    func_2()
    func_2()
    func_2()
    func_2()
    print("Who needs loops?")

#==========================================
# Purpose: Text adventure choice
# Input Parameter(s):
#text = question string
#optionA = answer choice option A
#optionB = answer choice option B
#optionC = answer choice option C
#path_1 = choose an answer to the text string question from A, B, or C
#
# Return Value(s): path_1
#=========================================

def choice(text, optionA, optionB, optionC):
    print(text)
    print("A.", optionA)
    print("B.", optionB)
    print("C.", optionC)
    path_1 = input("Choose A, B, or C.")
    if path_1 == "A":
        return path_1
    elif path_1 == "B":
        return path_1
    elif path_1 == "C":
        return path_1
    else:
        path_1 = "A"
        print("Invalid option, defulting to A.")
        return path_1

#==========================================
# Purpose: Text adventure game
# Input Parameter(s):
# "A" = activates one of the story's pathways
# "B" = activates one of the story's pathways
# "C" = activates one of the story's pathways
# 
# Return Value(s): booliean values -- True, False
#==========================================

def adventure():
    decision_1 = choice("What?", "Alpha", "Bravo", "Charlie")
    if decision_1 == "A":
        print("pass to level 2")
        decision_2 = choice("Who", "Friend", "Foe", "Civilian")
        if decision_2 == "A":
            print("Win!")
            decision_2 = True
            return decision_2
        elif decision_2 == "B":
            print("entering boss fight")
            decision_4 = choice("Where?", "9", "12", "3")
            if decision_4 == "A" or "B":
                print("Win!")
                decision_4 = True
                return decision_4
            else:
                decision_4 = False
                print("Lose!")
                return decision_4
        elif decision_2 == "C":
            print("jump to level 3")
            decision_3 = choice("When?", "Now", "Later", "Never")
            if decision_3 == "B":
                print("entering boss fight")
                decision_4 = choice("Where?", "9", "12", "3")
                if decision_4 == "A" or "B":
                    print("Win!")
                    decision_4 = True
                    return decision_4
                else:
                    print("Lose!")
                    decision_4 = False
                    return decision_4
            elif decision_3 != "B" or "C":
                print("Lose!")
                decision_3 = False
                return decision_3
            else:
                print("Win!")
                decision_3 = True
                return decision_3
    elif decision_1 == "C":
        print("jump to level 3")
        decision_3 = choice("When?", "Now", "Later", "Never")
        if decision_3 == "B":
            print("entering boss fight")
            decision_4 = choice("Where?", "9", "12", "3")
            if decision_4 == "A" or "B":
                print("Win!")
                decision_4 = True
                return decision_4
            else:
                print("Lose!")
                decision_4 = False
                return decision_4
        elif decision_3 != "B" or "C":
            print("Lose!")
            decision_3 = False
            return decision_3
        else:
            print("Win!")
            decision_3 = True
            return decision_3        
    elif decisoin_1 != "A" or "C" or "B":
        print("Invalid option, defulting to A.")
        print("pass to level 2")
        decision_2 = choice("Who", "Friend", "Foe", "Civilian")
        if decision_2 == "A":
            print("Win!")
            decision_2 = True
            return decision_2
        elif decision_2 == "C":
            print("jump to level 3")
            decision_3 = choice("When?", "Now", "Later", "Never")
            if decision_3 == "B":
                print("entering boss fight")
                decision_4 = choice("Where?", "9", "12", "3")
                if decision_4 == "A" or "B":
                    print("Win!")
                    decision_4 = True
                    return decision_4
                else:
                    print("Lose!")
                    decision_4 = False
                    return decision_4
            elif decision_3 != "B" or "C":
                print("Lose!")
                decision_3 = False
                return decision_3
            else:
                print("Win!")
                decision_3 = True
                return decision_3
    else:
        print("Lose!")
        decision_1 = False
        return decision_1
