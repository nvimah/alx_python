'''This class contains a method area that raises an exception'''
class BaseGeometry:
    '''In this class, we define the area() method, and when this method is called, it raises an Exception with the specified message "area() is not implemented". '''
    def area(self):
     '''In this class, we define the area() method, and when this method is called, it raises an Exception with the specified message "area() is not implemented".'''
    raise Exception("area() is not implemented")
'''on an instance of the derived class will raise the exception indicating that the method needs to be implemented in the subclass.'''