'''this is a class that contains a function that returns true if the object is exactly an istance ofthe specified class'''
def is_kind_of_class(obj, a_class):
    '''This function takes an object obj and a class a_class. It uses the isinstance() function to check if obj is an instance of a_class or if it's an instance of a class that inherited from a_class.'''
    return isinstance(obj, a_class)
'''If either condition is met, the function returns True, indicating that obj is a kind of the specified class. Otherwise, it returns False.'''