#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-04-02
Purpose: Rock the Casbah
"""

import argparse
import random
import os 
import string
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')


    parser.add_argument('-s',
                    '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.0)
                        
    args = parser.parse_args()

    if not 0 <= args.mutations < 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    num_mutations = round(len(text) * args.mutations)
    alpha = string.ascii_letters + string.punctuation
    new_text = text
    
    #random.sample(range(len(text)), num_mutations))
    for index in random.sample(range(len(text)), num_mutations):
        print(index)
        #print(text[index])
        new_char = random.choice(alpha)
        #print(new_char)
        new_text = new_text[:index] + new_char + new_text[index + 1:]
        

    print(f'You said: "{text}"')
    print(f'I heard : "{new_text}"')
    #print(f"I will change{num_mutations}.")

def random_string():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))    
         

# --------------------------------------------------
if __name__ == '__main__':
    main()
