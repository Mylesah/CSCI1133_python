
## Myles Halpern
## halpe084
import copy

# Part A: Red Blue Swap
#==========================================
# Purpose:
#   Swaps the red and blue components in an image
# Input Parameter(s):
#   A 3D matrix (list of lists of lists) representing an .bmp image
#   Each element of the matrix represents one row of pixels in the image
#   Each element of a row represents a single pixel in the image
#   Each pixel is represented by a list of three numbers between 0 and 255
#   in the order [red, green, blue]
# Return Value:
#   A 3D matrix of the same dimensions, with all colors inverted
#   (that is, for every pixel list, the first and last values have been
#   swapped.
#==========================================
def red_blue_swap(img_matrix):
    i = 0
    for row in img_matrix[:]:
        j = 0
        for column in row:
            temp0 = img_matrix[i][j][2]
            temp2 = img_matrix[i][j][0]
            img_matrix[i][j][0] = temp0
            img_matrix[i][j][2] = temp2
            j += 1                
        i += 1
    return img_matrix


# Part B: Grayscale
#==========================================
# Purpose:
#   Converts an image to grayscale
# Input Parameter(s):
#   A 3D image matrix (see part 1)
# Return Value:
#   A 3D matrix of the same dimensions, where each pixel has all components
#   (red, green, blue) set to a value determined by the formula:
#       0.3*red + 0.59*green + 0.11*blue
#   and then truncated down to the nearest integer.
#==========================================
def grayscale(img_matrix):
    i = 0
    for row in img_matrix[:]:
        j = 0
        for column in row:
           avg = int(img_matrix[i][j][0]*0.3 + img_matrix[i][j][1]*0.59 + img_matrix[i][j][2]*0.11)
           img_matrix[i][j][0] = avg
           img_matrix[i][j][1] = avg
           img_matrix[i][j][2] = avg       
           j += 1
        i +=1   
    return img_matrix
            
# Part C: Split
#==========================================
# Purpose:
#   Splits an image into four copies of itself, each with half the dimensions
#   of the original.  Computes each component of the output image's pixels by
#   taking the corresponding 2x2 square of pixels in the original and averaging
#   that component among those four pixels (truncating this average down to the
#   nearest integer).  See instructions for more details.
# Input Parameter(s):
#   A 3D image matrix (see part 1).  You may assume that the width and height
#   of the image are both even, so that each 1 pixel in the output image
#   corresponds to one 2x2 square of pixels in the input.
# Return Value:
#   A 3D matrix of the same dimensions, with the transformation described above.
#==========================================
def split(img_matrix):
    new_image = copy.deepcopy(img_matrix)
    value = []
    k = 0
    for rgb in range(3):
        i = 0
        for row in new_image[:]:
            j = 0
            for column in row:
                value.append(new_image[i][j][k])
                j += 1
            i += 1
        k += 1
    #print('value', value) #prints 16 values: the four values for r1, r2, g1, g2, b1, b2
    matrix = []
    x = 0
    y = 4
    for i in range(int(len(value)/4)):
        avg = 0
        avg = int((sum(value[x:y]))/4)
        matrix.append(avg)
        x +=4
        y +=4
    #print('avg value', matrix) #prints [avgr1, avgr2, avgg1, avgg2, avgb1, avgb2]
    i = 0
    j = int(len(matrix)/3)
    matrix_set = []
    for i in range(int(len(matrix)/3)):
        matrix_set.append(matrix[i::j])
    #print('mset', matrix_set) # prints [[avgr1, avgg1, avgb1], [avgr2....]]
    #final_matrix = []
    #a = 0
    #b = 2
    #for poo in range(2):
        #a = 0
        #b = 2
        #for pee in range(int(len(matrix_set)/2)):
            #final_matrix.append(matrix_set[a:b] * 2)
            #a += 2
            #b += 2
    #print(final_matrix)
    return matrix_set


# DO NOT EDIT ANYTHING BELOW THIS LINE

# Helper function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Compute the integer represented by a sequence of bytes
# Input Parameter(s):
#   A list of bytes (integers between 0 and 255), in big-endian order
# Return Value:
#   Integer value that the bytes represent
#==========================================
def big_end_to_int(ls):
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

# .bmp conversion function (you don't have to understand what this does)
#==========================================
# Purpose:
#   Turns a .bmp file into a matrix of pixel values, performs an operation
#   on it, and then converts it back into a new .bmp file
# Input Parameter(s):
#   fname, a string representing a file name in the current directory
#   operation, a string representing the operation to be performed on the
#   image.  This can be one of 3 options: 'invert', 'grayscale',
#   or 'split'.
# Return Value:
#   None
#==========================================
def transform_image(fname,operation):
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [red,green,blue].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i+2],data[i+1],data[i]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()

    #Perform operation on the pixel matrix
    if operation == 'red_blue_swap':
        new_matrix = red_blue_swap(matrix[::-1])
    elif operation == 'grayscale':
        new_matrix = grayscale(matrix[::-1])
    elif operation == 'split':
        new_matrix = split(matrix[::-1])
    else:
        return
    new_matrix = new_matrix[::-1]
    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i+2],data[i+1],data[i] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()

