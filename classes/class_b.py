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
    @property
    def materials(self):
        return self.__materials
    @materials.setter
    def materials(self, new_mat):
        '''we expect a list of materials'''
        if type(new_mat)==list and len(new_mat)>0:
            self.__materials = new_mat
        else:
            raise TypeError(f'{new_mat} is not an acceptable list of amterials')
    def __str__(self):
        # NB here we call the getter for each property
        return f'{self.name} is a {self.align} made of {self.materials}'

if __name__ == '__main__':
    wallace  = WG('Wallace', 'Goodie', ['plasticene', 'Silicone', 'Cheese'])
    feathers = WG('Feathers McGraw', 'Baddie', ['plasticene', 'wire', 'fingerprints'])
    print(wallace)
    print(feathers)