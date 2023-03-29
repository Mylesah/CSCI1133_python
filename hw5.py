#==========================================
# Purpose: Changes key for the inputed notes
# Input Parameter(s): notes: list of notes, up: number of key changes up
# Return Value(s): convert_notes
#==========================================

def convert(notes, up):
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    convert_notes = []
    elem = 0
    for elem in notes:
        convert_notes.append(scale[(scale.index(elem) + up) % len(scale)])
    return convert_notes


#==========================================
# Purpose: compares the sum of three numbers to see if they will equal the target value
# Input Parameter(s): num_lst: list of numbers, target: the value to compare the sum of the three numbers to
# Return Value(s): cycle
#==========================================

def triple_sum(num_lst, target):
    i = 0
    j = 0
    k = 0
    cycle = 0
    for i in range(len(num_lst)):
        for j in range(i+1, len(num_lst)):           
            for k in range (j+1, len(num_lst)):
                value = num_lst[i] + num_lst[j] + num_lst[k]
                if value == target:
                    print(num_lst[i],'+', num_lst[j],'+', num_lst[k],'=',target)
                    cycle += 1
    return cycle

#==========================================
# Purpose: Sorts a list of names based on if they have s, S, z, or Z in the string
# Input Parameter(s): names_list: list of names
# Return Value(s): grad_names
#==========================================

def no_front_teeth(names_list):
    read = []
    dont_read = []
    for name in names_list:
        if 'Z' in name:
            dont_read.append(name)
        elif 'S' in name:
            dont_read.append(name)
        elif 'z' in name:
            dont_read.append(name)
        elif 's' in name:
            dont_read.append(name)
        else:
            read.append(name)
    i = 0
    grad_names =[]
    if len(read) >= len(dont_read):
        while i in range(len(dont_read)):
            grad_names.append(read[i])
            grad_names.append(dont_read[i])
            i +=1
        k = len(read) - len(dont_read)
        for j in range(k):
            grad_names.append(read[i])
            i += 1
    else:
        print("Mission impossible: too many unpronounceable names")
    return(grad_names)
    
    






