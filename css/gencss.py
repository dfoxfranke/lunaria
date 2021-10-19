#!/usr/bin/env python3

import json

def to_css_rgba(rgb, a):
    return "rgba({0:.2f}%,{1:.2f}%,{2:.2f}%,{3:.3f})".format(
        *([ x * 100. for x in rgb] + [a])
    )

def camel_to_dashes(camel):
    dashes = list()
    for c in camel:
        if c.isupper():
            dashes.append("-")
            dashes.append(c.lower())
        else:
            dashes.append(c)
    return ''.join(dashes)

for (themename, themefile) in [("light", "../lunaria-light.json"), ("dark", "../lunaria-dark.json"), ("eclipse", "../lunaria-eclipse.json")]:
    theme = json.load(open(themefile))
    print(".lunaria-" + themename + " {")
    for (k,v) in theme.items():
        if k[0] == "_":
            continue
        print("  --lunaria-{}: {};".format(camel_to_dashes(k), to_css_rgba(v, 1.)))
        print("  --lunaria-{}-dodrantopaque: {};".format(camel_to_dashes(k), to_css_rgba(v, 0.75)))
        print("  --lunaria-{}-semiopaque: {};".format(camel_to_dashes(k), to_css_rgba(v, 0.5)))
        print("  --lunaria-{}-quadrantopaque: {};".format(camel_to_dashes(k), to_css_rgba(v, 0.25)))
        print("  --lunaria-{}-octantopaque: {};".format(camel_to_dashes(k), to_css_rgba(v, 0.125)))
    print("}")
