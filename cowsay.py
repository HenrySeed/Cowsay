#!/usr/bin/python

import sys

'''
A styled cowsay,
It uses a cleaner looking speech bubble.

So long as you're in the same directory you can just:

>>> from cowsay import *
>>> print(cowsay('Hello World'))
 _______________
/  Hello World  \
\_______________/
   V

    ^__^
    (oo)\_______
    (__)\       )\/\/
        ||----w\|
        ||     ||

(c) Henry Seed 2017
'''

def cowsay_splitter(string, line_length):
    '''returns string split into a list with each line being line_length long'''

    output = []                         # Passed out the end of the function
    words = string.split(' ')

    if len(string) <= line_length:      # only proceed if string is bigger than line_length
        output.append(string)
    else:

        while len(string) > line_length:    #
            total = 0
            line = ''
            while (total + len(words[0]) + 1) < line_length:
                line += words[0] + ' '
                total += len(words[0]) + 1
                words = words[1:]

            string = string[total:]
            output.append(line)

        if(string not in ['', ' ']):
            output.append(string)

    return output



def cowsay(message):
    '''returns a string of the message in a speech bubble above an ascii cow'''
    max_length = 0
    padding_len = 2
    padding = (padding_len*' ')
    line_length = 40
    result = ''
    if(len(message) < line_length):
        line_length = len(message)

    message = cowsay_splitter(message, line_length)

    cow = "    ^__^\n\
    (oo)\_______\n\
    (__)\       )\/\/\n\
        ||----w\|\n\
        ||     ||"

    line_length = int(line_length)
    result += (' ' + '_' * (line_length + (padding_len*2)) + '\n')
    result += ('/' + padding + message[0] + ((line_length - len(message[0])) * ' ') + padding + '\\\n')
    for i in message[1:]:
        result += ('|' + padding + i + ((line_length - len(i)) * ' ') + padding + '|\n')

    result += ('\\' + '_' * (line_length + (padding_len*2)) + '/\n')

    result += ('   V ' + '\n')
    result += ('\n')
    result += (cow)
    result += ('\n')

    return result


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        print(cowsay(' '.join(sys.argv[1:])))
