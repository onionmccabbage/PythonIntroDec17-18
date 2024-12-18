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
    @property
    def align(self):
        return self.__align
    @align.setter
    def align(self, new_align):
        # valid data is goodie, baddie, Goodie, Baddie
        if new_align.lower() in ('goodie', 'baddie'): # force to lower case to check
            self.__align = new_align
        else:
            self.__align = 'goodie'

    def __str__(self):
        pass

if __name__ == '__main__':
    wallace  = WG()
    feathers = WG()