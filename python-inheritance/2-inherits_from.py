'''This is a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.'''
def inherits_from(obj, a_class):
    '''This function takes an object obj and a class a_class. It first checks if obj is an instance of any class (i.e., of type object) using isinstance(obj, object).'''
    return  isinstance(obj, object) and issubclass(type(obj), a_class) and type(obj) is not a_class 
''' it checks if the type of obj (i.e., type(obj)) is a subclass of a_class using issubclass(type(obj), a_class). Finally, it makes sure that obj is not an instance of a_class itself by comparing type(obj) and a_class.'''