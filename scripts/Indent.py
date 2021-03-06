#!/usr/bin/env python

import sys
import argparse
import json
from collections import OrderedDict

def Indent(InFile, OutFile, givenIndent):

    try:
        with open(InFile) as infile:
            originalData = json.load(infile, object_pairs_hook=OrderedDict)
    except:
        sys.exit("%s: unable to open input file - perhaps malformed JSON?"%(OutFile))

    formattedResult = json.dumps(OrderedDict(originalData), indent=givenIndent, separators=(',', ': '))
    
    try:
        with open(OutFile, 'w') as outfile:
            outfile.write(formattedResult)
            outfile.write('\n')
    except:
        sys.exit("%s: unable to open outfile"%(OutFile))

#------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Slurp a JSON file and reformat indentation')
    parser.add_argument('-i',
        help='input file',
        required=True,
        nargs=1)
    parser.add_argument('-o',
        help='output file if specified, otherwise rewrite in place',
        required=False,
        nargs=1)
    parser.add_argument('--indent',
        help='indentation',
        required=False,
        nargs=1)
    args = parser.parse_args()

    indent = 2 if (args.indent==None) else int(args.indent[0])
    outfile = args.i[0] if (args.o==None) else args.o[0]
    Indent(args.i[0], outfile, indent)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main();
