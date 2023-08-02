'''this is a square class with a size attribute and several instances or objects of the square class '''
class Square:
    '''this is the first class named square that contains size attributes'''
    def __init__(self, size=0):
        self.size = size
        '''the size attribute is set to size as defined above before converting t to a private attribute'''
    def size (self):
        return self.__size
    '''the size attribute is changed to a private attribute by adding the double underscore'''
    def size(self, value):
      '''the size attribute is the changed to a value'''
      if not isinstance (value, int):
             raise TypeError ('size must be an integer')
      '''if the value for the size is not an integer raise a typeerror'''
    if size <= 0:
             raise ValueError ('size must be >= 0')
    '''if the value for the size is less than or equal to zero return valueerror'''
    def area (self):
         return self.__size ** 2
    '''calculates and returns the area of the square'''
    def my_print (self):
         if self.__size == 0:
              print()
              '''if the value of the size is equal to zero return an empty line'''
         else:
            for _ in range (self.__size):
                 print ("#" * self.__size)
                 '''else print a hashtag for every value keyed in'''
'''the class square and its atribute sizes and all of its instances are excecured'''
         
    
