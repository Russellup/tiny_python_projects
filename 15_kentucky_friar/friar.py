#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-06-21
Purpose: Rock the Casbah
"""

import argparse
import os
import re
import sys
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()


    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(type(args.text.splitlines()))
    for line in args.text.splitlines():
        print(line)
    #     print(''.join(fry(word) for word in re.split('(\W+)',line))

    # words = []
    # for word in re.split('(\W+)',line))
    # words.append(fry(word))

    # print(''.join)


# --------------------------------------------------
def fry(word):
#Anchor for character class
    you_match = re.match('[yY]ou', word)
    ing_match = re.search('(.*)ing$', word)

    # if you_match:
    #     return you_match.group(1) = "'all"

    # if ing_match:
    #     first = ing_match.group(1) 
    #     if re.search('(aeiou'), first, re.IGNORECASE):
    #         return first + "in'"    

    # if word.endswith('ing'):
    #     return word(:-1) = "'"

  




# --------------------------------------------------
def test_fry(word):

    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('your') == 'your'
    assert fry('fishing') == "fishin"
    assert fry('aching') == "Achin"
    assert fry('swing') == "swing"







# --------------------------------------------------
if __name__ == '__main__':
    main()
