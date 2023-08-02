class Square:
    '''
    This is a class that contains a square and will be use as a refernce to all the class instances
    '''
    def __init__(self, size):
        '''
        The init is used to allocate attributes to our class
        the first parameter references to the class
        the second parameter is the size attribute
        '''
        self.__size = size
        ''' 
         Initializes the square with a given size.
         size (int): The size of the square's side
         '''
my_square = Square
'''
This is used to calculete and return the value of the size
    '''
print()
