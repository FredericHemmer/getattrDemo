"""Dynamic functions

"""

class ArithmeticInt:
    """Implements arithmetic finctions and returns resulst as string

    """
    def __init__(self, register=None):
        if register is not None:
            for my_object in dir(self):
                if not my_object.startswith('_'):
                    register(my_object, getattr(self,my_object))

    def add (self, a, b):
        return a+b

    def mul(self, a,b):
        return a*b
