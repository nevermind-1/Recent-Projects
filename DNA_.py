import sys,time,random

PAUSE = 0.2 # Sleep length must be non-negative

# These are individual rows of the DNA animation
# Storing of the DNA strand data as an array.
ROWS =[
    #123456789
    '         ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '         #{}-{}#',
    #123456789
]
try:
    print('DNA Animation, by Ajuba okwuchukwu anthony')
    print('press ctrl-C to quit...')
    time.sleep(1)
    rowIndex = 0

    while 1:
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0
        if rowIndex == 0 or rowIndex == 9: # Row Indexes 0 and 9 have no nucleotides
            print(ROWS[rowIndex])
            continue
        #select random nucleotide pairs, guanine-cytosine and 
        # adenine-thymine
        random_select = random.randint(1,4)
        if random_select == 1:
            left_nucleotide,right_nucleotide = 'A','T'
        elif random_select == 2:
            left_nucleotide,right_nucleotide = 'T','A'
        elif random_select == 3:
            left_nucleotide,right_nucleotide = 'C','G'
        elif random_select == 4:
            left_nucleotide,right_nucleotide = 'G','C'

        print(ROWS[rowIndex].format(left_nucleotide,right_nucleotide))
        time.sleep(PAUSE) #Adding a slight pause in the execution of the program

except KeyboardInterrupt:

    sys.exit() # End the program when ctrl-C is pressed


