#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-03-06
Purpose: Gashlycrumb
"""

import argparse
import os
import sys
from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        help='Letter(s)',
                        metavar='letter',
                        nargs = '+',
                        type=str)

    
    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    #print('letter',args.letter)

    lookup = dict()
    
    for line in args.file:
    
         lookup[line[0].upper()] = line.rstrip()
        
         #pprint(lookup) 
         #print('line(0)',line[0]) 
         #print('line(0).upper()',line[0].upper() ) 
         #print ('line', line)     
    
    for letter in args.letter:
        #print(lookup)
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:   
            print(f'I do not know "{letter}".')
    
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
