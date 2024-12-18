def letsFindOut():
    '''can we use slots within a function'''
    __slots__ = ['__x'] # pointless - __slots__ only work within a class
    # what about mangling...
    __x = 'test' # yep - we can use name mangling within any structure

letsFindOut.__canWeDoThis = 'ummmmm'
# print(letsFindOut.__x) # this should fail (due to name-mangling)


class Weather():
    '''
    The Weather class takes a string for the description
    and a floating point number or integer for the temperature
    '''
    # NB slots SHOULD be names with __
    __slots__ = ['__city','__desc', '__temp']
    def __init__(self, city, desc, temp):
        self.city = city # this will call the city setter method
        self.desc = desc
        self.temp = temp
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        # or isinstance(new_city, str)
        if type(new_city) == str and len(new_city)>2:
            self.__city = new_city # name-mangling so there is no aces to this outside the class
        else:
            self.__city = 'Athlone'
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        if type(new_desc) == str:
            self.__desc = new_desc
        else:
            self.__desc = '' # default to an empty string
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        if type(new_temp) in (int, float):
            self.__temp = new_temp
        else:
            self.__temp = 12 # a reasonable default
    def __str__(self):
        # output a nicely formatted weather report       format to specific decimal places
        report  = f'The weather in {self.city} is {self.desc} at {self.temp:0.2f}C'
        return report


if __name__ == '__main__':
    # exercise this module
    w_gen = Weather('Genoa', 'rainy', 9.04)
    w_gal = Weather('Galway', 'windy', 6.70)
    w_kt  = Weather('Kingston', 'sunny', 27.98)
   
    print(w_gen)
    print(w_gal)
    print(w_kt)

    w_default = Weather(False, [], ()) # wrong data types so should fall back to the defaults
    print(w_default)
