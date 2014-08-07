#! /usr/bin/python3.4

from os import listdir
import re

# Generate empty dictionary
filenames={}

# Generate values and populate dictionary
path='./babynames/'
f=[f for f in listdir(path) if f[-4:]=='html'] # List of file names in the relevant directory, ending in 'html'

for f in f:
    year=int(f[-9:-5])
    with open(path+f, 'r', encoding='utf8') as f:   
        filenames[year]=f.read()


# Compile the regex for recurring use below.
babynames=re.compile('(\d+)<.*>(\w+)<.*>(\w+)') 


while True:
    year=input('\nOnly even years during 1990-2008 available. Which year would you like to see (Enter to exit)? ')
    if year:
        try:
            year=int(year)
            while True:
                if year in filenames.keys():
                    break 
                else:
                    year=int(input('That year is not available, try again: '))
            names=re.findall(babynames, filenames[year])
            names=[ names[i][j]+' '+names[i][0] for i in range(len(names)) for j in (1,2) ] 
            #print(str(year)+'\n','\n'.join(sorted(names)))
            print(str(year), *sorted(names), sep='\n') # Using argument unpacking instead of join!

        except ValueError as err:
            print(err, '\n\nThat is not a year. Try again.') 
            continue
    else:
        print('\n\nBye!\n\n')
        break
