'''This is a csquare class that has a size attribute'''
class Square:
    '''This is the square class'''
    def __init__(self, size=0):
        self.size = size
        '''The size attribute is set to size'''
        def size(self):
            return self.__size
        '''size is allocated a private attribute'''
        def size(self, value):
         '''size is cahanged to value'''
         if not isinstance (value, int):
            raise TypeError ("size must be an integer")
         '''typeerror is raised if the size is not an integer'''
         if size < 0:
            raise ValueError ("size must ne >= 0")
         '''value error is raised if a negetive number or zero is input'''
         self.__size = value
         '''the private attribute size is set to value'''
        def area (self):
            return self.__size ** 2
        '''the area of the square is printed and retuended'''
        