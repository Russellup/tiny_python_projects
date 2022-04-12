#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-03-04
Purpose: Jump the five 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar ='str', help = 'input text')
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
     '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    
    new_text = []
    for char in list(text):
        new_text.append(jumper.get(char, char))

        
    
    print(''.join(new_text))
# --------------------------------------------------
if __name__ == '__main__':
    main()
