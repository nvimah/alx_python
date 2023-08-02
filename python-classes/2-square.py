'''
This is a class square that defines the size of a square
'''
class Square:
    '''This is a class that defines the size of a square'''
    def __init__(self, size=0):
        '''The size of the square is set to zero'''
        if not isinstance (size, int):
            raise TypeError ("Size must be an integer")
        '''Typeerror is raised when the size value is not an integer'''
        if size < 0:
            raise ValueError ("size must be >= 0")
        '''Value error is raised if a negative number is input'''
        self.__size = size
        '''size is allocated a private attribute'''
    def area (self):
       '''This function calculates the area of  a square'''
       return self.__size ** 2
    '''The area is then returned'''
     
        