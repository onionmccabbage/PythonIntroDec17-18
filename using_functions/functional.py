# imagine a heating/cooling system controled by our Pythno code
# too hot -> cooling and too cold -> heating

# the names of variables: letters, numbers, underscore. Don't start with a digit

def controlAC(temperature):
    '''turn heater and cooling on or off based on temperature'''
    if temperature < 18:
        return 'Heater on'
    elif temperature > 28:
        return 'AC on'
    else:
        return 'Just right'
    
def findAverage(tup):
    '''calculate the average of all the numbers in a tuple'''
    numValues = len(tup)
    total = 0
    for i in tup:
        total += i
    return total/numValues 


# we write the following line to ensure the exercise-code only runs
# when we run this module directly (not via import)
if __name__ == '__main__':
    # exercise the code
    print( controlAC(13) )
    print( controlAC(33) )
    print( controlAC(-12) )
    print( controlAC(24) )
    t = (1,2,3,4,5)
    print( findAverage(t) ) # 3