class WG():
    '''This class will hold a non-empty string for name
    a 'goodie' or 'baddie' value for alignment 
    a list of materials'''
    __slots__ = ['__name', '__align', '__materials']
    def __init__(self, n, a, m):
        self.name      = n
        self.align     = a
        self.materials = m
    @property # name getter
    def name(self):
        return self.__name
    @name.setter # name setter
    def name(self, new_name):
        if type(new_name)==str and new_name !='':
            self.__name = new_name

    def __str__(self):
        pass

if __name__ == '__main__':
    wallace  = WG()
    feathers = WG()