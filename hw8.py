#==========================================
# Purpose: helper function to check if the file being opened exists
# Input Parameter(s): fname_in: the name of the file you're checking
# Return Value(s): -1 (if the file doesn't exist) and 0 (if the file does exist)
#==========================================

import math

def file_exists(fname_in):
    try:
        fp = open(fname_in, 'r')
        return 0
    except FileNotFoundError:
        return -1

#==========================================
# Purpose: takes a 3d object file and creates a new file from the object in the original file, but rotated
# and checks to make sure the file exists by return -1 for not existing or 0 if it does exist
# Input Parameter(s): fname_in: is the name of the 3d object file you want to rotate
#fname_out: is the name of the ne 3d object file after it has been rotated using the original file
# Return Value(s): -1 (if the file doesn't exist) and 0 (if the file does exist)
#==========================================
def rotate_model(fname_in, fname_out):
    if file_exists(fname_in) == 0:
        fp = open(fname_in, 'r')
        lines = fp.readlines()
        rotated_lines = []
        stringed = ''
        for line in lines:
            line_list = line.split(' ')
            if line_list[0] == 'v':
                x = float(line_list[1]) #line_list[1] is x, line_list[2] is y
                y = float(line_list[2]) 
                x_rotated = str(x * math.cos(math.pi/2) + y * math.sin(math.pi/2))
                y_rotated = str(y * math.cos(math.pi/2) + x * math.sin(math.pi/2))
                line_list[1] = x_rotated
                line_list[2] = y_rotated
                rotated_str = ' '.join(line_list)
                stringed += rotated_str
            elif line_list[0] == 'f':
                stringed += line
        fp.close()
        fp = open(fname_out, 'w')
        fp.write(stringed)
        fp.close()
    return(file_exists(fname_in))

        

#B. Part 1: get_data_list
#==========================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#==========================================
def get_data_list(fname):
    try:
        fp = open(fname, 'r')
    except FileNotFoundError:
        return -1
    lst = []
    for line in fname:
        lst.append(fp.readline())
    fp.close()
    return lst    

#B. Part 2: get_col_index
#==========================================
# Purpose:
#   Determine which column stores a specific value
# Input Parameter(s):
#   row1_str is a string containing the first row of data 
#   (the column titles) in the CSV file
#	col_title is a string containing the column title
# Return Value:
#   Returns the index of the column specified by col_title
#   OR returns -1 if there is no column found
#==========================================
def get_col_index(row1_str, col_title):
    try:
        col_title in row1_str == True
        row_lst = row1_str.split(',')
        return row_lst.index(col_title)
    except ValueError:
        return -1

#B. Part 3: convert_dkp
#==========================================
# Purpose:
#   Covert the DKP in your row string to the new system
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to the new DKP (as a string)
#==========================================
def convert_dkp(row_str,idx):
    row_lst = row_str.split(',')
    row_lst[idx] = str(float(row_lst[idx]) *13.7)
    row_str = ','.join(row_lst)
    return row_str

#B. Part 4: merge_guild
#==========================================
# Purpose:
#   Alters a DKP CSV file to convert DKP after a guild merger
# Input Parameter(s):
#   fname is the file name of the DKP file
# Return Value:
#   Returns False if the file isn't open
#   Returns False if the file doesn't contain 'DKP' and 'Original Guild' columns
#   Otherwise, returns True
#==========================================
def merge_guild(fname):
    file_lst = get_data_list(fname)
    if get_data_list(fname) == -1:
        return False
    elif get_col_index(file_lst[0],'DKP') == -1:
        return False
    elif get_col_index(file_lst[0],'Original Guild') == -1:
        return False
    else:
        f_idx = fname.index('.')
        new_fname = fname[0:f_idx]+ '_correct.csv'
        file_lst = get_data_list(fname)
        og_indx = get_col_index(file_lst[0], 'Original Guild')
        dkp_indx = get_col_index(file_lst[0], 'DKP')
        row_num = 0
        file_str = ''
        for row in file_lst:
            if 'Lions of Casterly Rock' in row:
                row_conv = convert_dkp(row, dkp_indx)
                file_str += row_conv
            else:
                file_str += row
            row_num += 1
        fp = open(new_fname, 'w')
        fp.write(str(file_str))
        fp.close()
        return True


 
