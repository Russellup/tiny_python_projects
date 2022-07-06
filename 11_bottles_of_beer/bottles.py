#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-04-02
Purpose: Rock the Casbah
"""
import argparse
from hashlib import shake_128
import os 
import sys

#-------------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Sing bottles of beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-n',
                       '--num',
                       help='Number of Verses',
                       metavar='number',
                       type=int,
                       default=10)
    
    args = parser.parse_args()

    if args.num < 1:
        parser.error(f' --num (args.num) must > 0')
    
    
    return args

#--------------------------------------------------------------
def main():

    args = get_args()
    
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))    


#----------------------------------------------------------------
def verse(bottle):


    next_bottle = bottle - 1
    s1 = ''if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    next_num = 'No More' if next_bottle == 0 else next_bottle

    return '\n'.join([
          f'{bottle} bottle{s1} of beer on the wall,', 
          f'{bottle} bottle{s1} of beer,',
          'Take one down, pass it around,',
          f'{next_num} bottle{s2} of beer on the wall!'
          ])



def test_verse(bottle):

      one = verse(1)
      assert one == '\n'.join([
          '1 bottle of beer on the wall,', '1 bottle of beer,',
          'Take one down, pass it around,',
          'No more bottles of beer on the wall!'
          ])

      two = verse(2)
      assert two == '\n'.join([
          '2 bottles of beer on the wall,', '2 bottles of beer,',
          'Take one down, pass it around,', '1 bottles of beer on the wall!'
          ])


#----------------------------------------------------------------

if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
