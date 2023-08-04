'''This class contains a method area that raises an exception'''
class BaseGeometry:
    '''In this class, we define the area() method, and when this method is called, it raises an Exception with the specified message "area() is not implemented". '''
    def area(self):
     '''In this class, we define the area() method, and when this method is called, it raises an Exception with the specified message "area() is not implemented".'''
     raise Exception("area() is not implemented")
    '''this method defines a name attribute and a value attribute'''
def integer_validator(self, name, value):
 ''' we've added the integer_validator() method. This method takes two arguments: name (a string representing the name of the value being validated) and value (the value to be validated).'''
 if not isinstance(value, int ):
   '''The method checks if value is an integer using isinstance(value, int). If not, it raises a TypeError exception with the message "<name> must be an integer".'''
   raise TypeError(f"{name} must be an integer")
 '''Next, the method checks if the value is less than or equal to 0. If it is, it raises a ValueError exception with the message "<name> must be greater than 0".'''
 if value<= 0:
   raise ValueError(f"{name} must be greater than 0")
 '''his integer_validator() method can be used by derived classes to validate integer inputs before performing any specific calculations related to the area or any other calculations.'''
       
'''This is a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).'''
class Rectangle(BaseGeometry):
    '''In this implementation, we create the Rectangle class, which inherits from the BaseGeometry class.'''
    def __init__(self, width, height):
     '''The Rectangle class has a constructor (__init__) that takes width and height as arguments.''' 
     self.__width = width
     self.__height = height
     self.integer_validator("width",  self.__width)
     self.integer_validator("height", self.__height)
     '''We use the integer_validator() method inherited from the BaseGeometry class to validate that width and height are positive integers.'''
    def area(self):
      return self.__width * self.__height
    

    def __str__(self):
      return f"[Rectangle] {self.__width}/{self.__height}" 