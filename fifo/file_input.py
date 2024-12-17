# to retrieve text from a file we use a file accessobjet, similar to this...

def readText():
    '''access the text from a file'''
    try:
        # NB for code-hinting try ctrl-space
        fin = open('file.txt', 'rt') # 'rt' will read text
        with fin:
            retrieved = fin.read() # read all the contents as one long string of text
            # remember the file access object will close when we are done
        return retrieved
    except Exception as err:
        print(f'A general problem occured: {err}')

# we may exercise the code
r = readText() # call the function
print(r)