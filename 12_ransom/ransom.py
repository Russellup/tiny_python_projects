#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-05-23
Purpose: Create a ransom note
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create a ransom note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')
    parser.add_argument('-s',
                    '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)
    

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args     
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    #new_text = ''

    #for char in args.text:
    #    new_text += choose(char)

    #new_text = (choose(char) for char in args.text
    #print(''.join([choose(char) for char in args.text]))    
    new_text = map(choose, args.text)
    print(''.join(new_text))
# --------------------------------------------------
def choose(char):

   return char.upper() if random.choice([0,1]) else char.lower()

#-------------------------------------------------------
def test_choose():


    state = random.getstate()
    random.seed(1)
    assert choose('a') =='a'
    assert choose('b') =='b'
    assert choose('C') =='C'
    assert choose('d') =='d'
    random.setstate(state)





#-------------------------------------------------------
if __name__ == '__main__':
    main()
