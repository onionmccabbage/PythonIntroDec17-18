# Comma-separated-Variables (csv) are very common as a simple way to structure text files
h = 'Floela, 42, admin, Python'
j = 'Jane, 32, user, SQL'
k = 'Ade, 84, guest, Java'

# we can manipulate strings of text
m = h.split(', ') # make a list containing the separate data
print(m, type(m))

# we may write csv to a text file
def writeCSV(c):
    '''write the incoming text to a file'''
    try:
        fout = open('content.csv', 'at')
        with fout:
            fout.write(f'{c}\n') # choose to add a new line character
    except Exception as err:
        print(f'Problem: {err}')

# exercise the code
writeCSV(h)
writeCSV(j)
writeCSV(k)