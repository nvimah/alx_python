'''
This is a class that defines a square based on the predifined size
'''
class Square:
    '''
    This is the class square that has a size attribute
    '''
    def __init__(self, size=0) :
       if not isinstance(size, int):
            raise TypeError("size must be an integer")
            '''
            returns True if the specified object is of the specified type, otherwise False
            '''
       if size < 0:
            raise ValueError("size must be >= 0")
            '''
            returns True if the specified object is of the specified type, otherwise False
            '''
       self.__size = size
