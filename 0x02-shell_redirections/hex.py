#!/usr/bin/python3

import argparse

base_conversion = {
    "oct": (lambda x: f"{oct(x)[1:]}{0}"),
    "hex": (lambda x: hex(x)),
    "dec": (lambda x: x)
}

parser = argparse.ArgumentParser(
            prefix_chars='-',
            allow_abbrev=True
        )

parser.add_argument('-i', 
                    required=True,
                    dest="input_string",
                    help="THE STRING YOU WANT TO CONVERT INTO OCTAL, HEX, OR DECIMAL."
                )
parser.add_argument('--base',
                    '-b',
                    choices=list(base_conversion.keys()),
                    default="hex",
                    required=False,
                    dest="base",
                    help="THE BASE YOU WOULD LIKE TO CONVERT THE STRING TO (OCTAL OR HEX)"
                )
args = parser.parse_args()

conversion = base_conversion[args.base]
input_string = args.input_string 

out_string =  "".join([f"{chr(92)}{conversion(ord(x))[1:]}" for x in [*input_string]])

print(out_string)