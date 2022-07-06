#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-06-06
Purpose: Rhyming words
"""

import argparse
import os
import sys
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create rhyming words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The word to rhyme')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    prefixes = list('bcdfghjklmnpqrstvwxyz') + ('bl br ch cl cr dr fl fr gl gr pl pr sc'
    'sh sk sl sm sn sp st sw th tr tw thw wh wr'
    'sch scr shr sph spl spr squ str thr').split()

    start, rest = stemmer(args.word)

    if rest:

     words = '\n'.join(sorted([p + rest for p in prefixes if p != start]))
     print(words)
    else:
     print(f'Cannot rhyme"{args.word}"')

# --------------------------------------------------
def stemmer(word):

   word = word.lower()
   
   vowels = 'aeiou' 
   consonants = ''.join([c for c in string.ascii_lowercase if c not in vowels])    
   pattern = f'([{consonants}]+)?([{vowels}].*)?'
   
   print(pattern)
   
   match = re.match(pattern, word.lower())
   
   
  
         
   return (match.group(1) or '', match.group(2) or '') if match else('','')


# --------------------------------------------------

def test_stemmer():
    assert stemmer('') == ('','')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch','air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()

   # the addition sign inside of regex is a special symbol
   # it m 
