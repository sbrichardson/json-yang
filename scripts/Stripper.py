#!/usr/bin/env python

import sys
import re
import argparse
import json
from collections import OrderedDict

pattern = re.compile("//")
def Stripper(InFile, OutFile, Clean, Indent):

    try:
        with open(InFile) as infile:
            # OrderedDict is necessary to preserve JSON order to Python dict
            originalData = json.load(infile, object_pairs_hook=OrderedDict)
    except:
        sys.exit("%s: unable to open input file - perhaps malformed JSON?"%(OutFile))

    # do the work
    filteredData = traverse(originalData, Clean)

    formattedResult = json.dumps(filteredData, indent=Indent, separators=(',', ': '))
    try:
        with open(OutFile, 'w') as outfile:
            outfile.write(formattedResult)
            outfile.write('\n')
    except:
        sys.exit("%s: unable to open outfile"%(OutFile))

#------------------------------------------------------------------------------
def traverse(d, Clean):
    if isinstance(d, dict):
        for k in list(d.keys()):
            if (pattern.search(k) and Clean):
                del d[k]
            else:
                traverse(d[k], Clean)
    elif isinstance(d, list):
        for j in d:
            traverse(j, Clean)
    return d

#------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Strip pseudo-comments from JSON')
    parser.add_argument('-i',
        help='input file',
        required=True,
        nargs=1)
    parser.add_argument('-o',
        help='output file if specified, otherwise rewrite in place',
        required=False,
        nargs=1)
    parser.add_argument('--indent',
        help='JSON indentation',
        required=False,
        nargs=1)
    parser.add_argument('--clean',
        action='store_true',
        required=False,
        help='remove all comments')
    args = parser.parse_args()

    indent = 2 if (args.indent==None) else int(args.indent[0])
    outfile = args.i[0] if (args.o==None) else args.o[0]
    Stripper(args.i[0], outfile, args.clean, indent)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main();

