#!/usr/bin/env python3

import argparse
import json
import sys
import textwrap

def to_css_hex(rgb):
    return "#{0:02X}{1:02X}{2:02X}".format(
        *[ round(x * 255.) for x in rgb ]
    )

def to_css_rgb(rgb):
    return "rgb({0:.2f}%,{1:.2f}%,{2:.2f}%)".format(
        *[ x * 100. for x in rgb]
    )

def to_decimal_rgb(rgb):
    return "{0:d},{1:d},{2:d}".format(
        *[ round(x * 255.) for x in rgb]
    )

def calc_opacity_rgb(rgb_fg, rgb_bg, alpha):
    return [alpha * c1 + (1 - alpha) * c2 for (c1, c2) in zip(rgb_fg, rgb_bg)]

def inject_bg_opacity_colors(theme):
    alpha_levels = [0.75, 0.5, 0.25, 0.125]
    bg_colors = [
        "bgRed",
        "bgYellow",
        "bgGreen",
        "bgBlue",
        "bgDarkBlue",
        "bgLightYellow",
        "bgHighlight",
        "bgLowlight"
    ]

    for c in bg_colors:
        for l in alpha_levels:
            color_name = "%s"
            theme["{}/{}".format(c, l)] = calc_opacity_rgb(theme[c], theme["bg"], l)

    return theme


FORMATTERS = {
    "css_hex": to_css_hex,
    "css_rgb": to_css_rgb,
    "decimal_rgb": to_decimal_rgb
}

def main():
    parser = argparse.ArgumentParser(description="Insert Lunaria colors into a template", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('theme', type=str, help="JSON file defining theme colors")
    parser.add_argument('input', type=str, nargs='?', help="Template file (default: stdin)")
    parser.add_argument('output', type=str, nargs='?', help="Output file (default: stdout)")

    parser.add_argument('--format', type=str, choices=FORMATTERS.keys(), default="css_hex",
    help=textwrap.dedent('''\
    How to format color codes

    A neutral gray would be formatted as follows:

    css_hex:      #808080
    css_rgb:      rgb(50.00%%,50.00%%,50.00%%)
    decimal_rgb:  128,128,128

    The default is 'css_hex'
    '''))

    args = parser.parse_args()

    formatter = FORMATTERS[args.format]
    if args.input is None:
        infile = sys.stdin
    else:
        infile = open(args.input, 'r')

    if args.output is None:
        outfile = sys.stdout
    else:
        outfile = open(args.output, 'w')

    themefile = open(args.theme, 'r')
    theme = json.load(themefile)
    theme = inject_bg_opacity_colors(theme)

    for line in infile:
        for (k,v) in theme.items():
            if k[0] == '_':
                line = line.replace("@" + k + "@", v)
            else:
                line = line.replace("@" + k + "@", formatter(v))
        outfile.write(line)

if __name__ == "__main__":
    main()
