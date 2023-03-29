
#==========================================
# Purpose: objects represent imaginary numbers
# Instance variables: real: an integer representing a real number,
# imag: an integer representing an imaginary number
# Methods: __init__: initializes the variables, get_real/imag: returns the real/imag values of your class object
# set_real/imag: changes the value of real/imag inside the class object, __str__: overloads the print/str functions with a specific format
# __add__: overloads the addition operator, __mul__: overloads the multiplication operator,
# __eq__: overloads the equal ('==') operator
#==========================================
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def get_real(self):
        return self.real
    def get_imag(self):
        return self.imag
    def set_real(self, new_real):
        self.real = new_real
    def set_imag(self, new_imag):
        self.imag = new_imag
    def __str__(self):
        return '{} + {}i'.format(self.real, self.imag)
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)
    def __mul__(self, other):
        rr_val = self.real * other.real
        ri_val = (self.real * other.imag) + (self.imag * other.real)
        ii_val = self.imag * other.imag
        real = rr_val + (ii_val * -1)
        imag = ri_val
        return Complex(real, imag)
    def __eq__(self, other):
        if self.real == other.real:
            if self.imag == other.imag:
                return True
            else:
                return False
        else:
            return False

#==========================================
# Purpose: objects represent a retail store item
# Instance variables: name: name of the item (a string), price: price (as a float number) of the item,
# category: the type of clothing object (a string), store: the name of the store (a string)
# Methods: __init__: initializes the variables, __str__: overloads the print/str functions with a specific format,
# __lt__: overloads the less then operator to compare an Item class price
#==========================================
class Item:
    def __init__(self, name, price, category, store):
        self.name = name
        self.price = price
        self.category = category
        self.store = store
    def __str__(self):
        return "{}, {}, {}: ${}".format(self.name, self.category, self.store, self.price)
    def __lt__(self, other):
        if self.price < other.price:
            return True
        else:
            return False

#==========================================
# Purpose: object represents a Store derived from Item class
# Instance variables: name: the name of the store, filename: the name of the store's inventory csv file,
# items: a list of Item class objects that are representing everything inside a store
# Methods: _init__: initializes the variables, __str__: overloads the print/str functions with a specific format
#==========================================
class Store(Item):
    def __init__(self, name, filename):
        self.items = []
        self.name = name
        fp = open(filename, 'r')
        for line in fp:
            line = line.strip()
            x = line.split(',')
            if '.' in x[1]:
                y = Item(x[0], float(x[1]), x[2], name)
                self.items.append(y)
        fp.close()
    def __str__(self):
        string = self.name
        for line in self.items:
            string += '\n' + Item.__str__(line)
        return string

#==========================================
# Purpose: takes in a list of Store objects and returns a dictionary of the cheapest item for each Item class object
# Input Parameter(s): store_list: a list of Store objects
# Return Value(s): cheapest: a dictionary each key is a item category
# and each value is an Item class object with the cheapest price 
#==========================================      
def cheap_outfit(store_list):
    cheapest = {}
    for i in store_list:
        for j in i.items:
            if j.category not in cheapest:
                cheapest[j.category] = j
            elif j.category in cheapest:
                k = cheapest[j.category]
                if Item.__lt__(j, k) == True:
                    cheapest[j.category] = j
    return cheapest

