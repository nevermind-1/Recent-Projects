from email import message
import sys

# THere are 68 periods along the top and bottom of this string

bitmap = '''
....................................................................
    ***************   *   ***   **  *       ************************
   ***********************  **** ****   *   **********************  *
**      *************                   *************************
        ***********                  *****  *****************
        *******                      ****       **************
        ****                      *******      **********
        *****                   *********       *****
        *******             **********          ******
      *******               ***********        ********
      ****                    ********  **      ****
    ***********         ************    **  *   *********
    *****   ****    *************** ****    ******* ****    **  
....................................................................
'''
print('Bitmap Message, by ajuba okwuchukwu anthony')
print('Enter the message tp display with the bitmap.')
message = input('> ')
if message =='':
    sys.exit()

#loop throgh each of the line in the bitmap:
for line in bitmap.splitlines():
    #loop through over each character in the line:
    for i,bit in enumerate(line):
        if bit == ' ':
            print(' ',end ='')
        else:
            print(message[i % len(message)], end = '')
    print()