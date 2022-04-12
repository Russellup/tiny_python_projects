#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-03-21
Purpose: Rock the Casbah
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel',
                        metavar='str',
                        type=str,
                        choices='aeiou',
                        default='a')

    

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    

    print('text = "{}"',format(text))
    print('vowel = "{}"',format(vowel))
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
