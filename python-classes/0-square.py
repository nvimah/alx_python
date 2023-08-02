class Square:
    def __init__(self, _size):
        self._size = _size
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)