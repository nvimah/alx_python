'''this is a class that contains a function that returns true if the object is exactly an istance ofthe specified class'''
def is_same_class (obj, a_class):
    '''This function takes an object obj and a class a_class. It uses the type() function to get the class of obj and then compares it with a_class.'''
    return type(obj) is a_class
''' If they are the same, it returns True, indicating that obj is an instance of the specified class. Otherwise, it returns False.'''