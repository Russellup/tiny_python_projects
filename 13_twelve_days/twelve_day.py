#!/usr/bin/env python3
"""
Author : hongm <hongm@localhost>
Date   : 2022-05-26
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='File',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-n',
                        '--num',
                        help='number of days',
                        metavar='days',
                        type=int,
                        default=12)

    

    args = parser.parse_args()
    
    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('======')
    print(args)
      
    #out_fh = open(args.outfile, 'wt')if args.outfile else sys.stdout)

    #verses = []
    #for day in range( 1, args.num + 1):
    #    verses.append(verse(day))
        
    verses = (verses(day) for day in range(1, args.num + 1))

    verses = map(verse, range(1, args.num + 1))    
        
    print('\n\n'.join(verses), file =args.outfile)

# --------------------------------------------------
def verse(day):
    
    ordinal = ['first', 'second', 'third', 'fourth',
    'fifth', 'sixth', 'seventh', 'eighth', 'nineth', 'tenth',
    'eleventh', 'twelfth'
    ]

    gifts = [ 
        'A partridge in a pear tree,', 'Two turtle doves,',
        'Three french hens,',
        'Four calling birds,',
        'Five golden rings,',
        'Six geese a laying,',
        'Seven swans a swimming,', 'Eight maids a milking,', 'Nine ladies,',
        'Ten lords a leaping,', 'Eleven pipers piping,', 'Twelve drummers drumming'
    ]







    lines = [
            f' On the {ordinal[day - 1]} day of christmas,',
            'my true love gave to me ,']
    
    
    for n in range(day, 0, -1 ):
        lines.append(gifts[n - 1])
    
    lines.extend(reversed(gifts[:day]))


    if day > 1:
        lines[-1] = 'And' + lines[-1].lower()

    return '\n'.join(lines)    



#----------------------------------------------------
def test_verse():



        assert verse(1) == '\n'.join([
        'On the first day of christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.' ]) 
        assert verse(2) == '\n'.join([
        'On the second day of christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
         ])
    
    



#---------------------------------------------------
if __name__ == '__main__':
    main()
