#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-07-01
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import re



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble words in text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='input text')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    

    args = parser.parse_args()
    print('if', os.path.isfile(args.text))
    if os.path.isfile(args.text):
        print('justins hair is dope')
        args.text = open(args.text).read().rstrip()
      
        return args
    else: 
        print('args.text was not a file')    
        return 


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args == None:
        print('args was None')
        return 
    print('type(args)', type(args))
    print('type(random)', type(random))
    

    random.seed(args.seed)
    splitter = re.compile("([a-zA-z](?:[a-zA-Z']*[a-zA-Z])?)")

    for line in args.text.splitlines():
      print(''.join([scramble(word) for word in splitter.split(line)]))  
      

# --------------------------------------------------

def scramble(word):

    if len(word) >= 3 and re.match(r'\w+', word):
        middle = list(word[1: -1])
        random.shuffle(middle)
        word = word[0] + '' .join(middle) + word[-1]

    return word    





# --------------------------------------------------
def test_scramble():

    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "abcd"
    assert scramble("abcde") == "abcde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)






# --------------------------------------------------
if __name__ == '__main__':
    main()
