# Lunaria

Lunaria is a family of soothing, moderate-contrast color palettes for terminals,
text editors, and technical documentation. Lunaria's colors were generated
algorithmically, employing the cutting edge of color science: the CAM16 color
appearance model and its associated uniform color space and chromatic adaptation
transform. Lunaria includes three distinct palettes:

* The *Light* palette is for users who prefer to read dark text on a light
  background. It is designed to provide the best facsimile of ink-on-paper that
  an LCD monitor can possibly achieve. Its colors are optimized for viewing in
  the bright window-lit conditions typical of 21st century office buildings, but
  hold up well in a broad range of conditions.

* The *Dark* palette is for users who prefer light text on a dark background.
  Its neutral colors are designed to give an impression of a moonlit night and
  are derived from actual spectral data collected from the Fred Lawrence Whipple
  mountaintop astronomical observatory. It is optimized for nighttime viewing
  under dim, warm LED illumination.

* The *Eclipse* palette is almost identical to the Dark palette, but optimized
  for the same brighter viewing conditions as the Light palette is. The most
  visible difference is that the background is darker as a result of
  compensating for increased viewing flare (ambient light reflected off the
  monitor surface).

## What's here

For a detailed, designer-focused introduction to Lunaria and how to use it in
your own work, see <https://lunaria.design>. All other "official" Lunaria
resources are here in this repo.

* The files [lunaria-light.json](./lunaria-light.json),
  [lunaria-dark.json](./lunaria-dark.json), and
  [lunaria-eclipse.json](./lunaria-eclipse.json)
  canonically define the respective color palettes.

* [lunarize.py](./lunarize.py) is a script for substituting color definitions
  (provided by one of the above JSON files) into a template.

* [lunaria.ipynb](./lunaria.ipynb) is the Jupyter notebook which was used to
  generate Lunaria. Go here if you're interested in the gory mathematical
  details of how it was constructed.

* [vscode/](./vscode/) contains the sources of the Lunaria extension for Visual
  Studio Code. (End-users are best off obtaining this through the
  [Marketplace](https://marketplace.visualstudio.com/items?itemName=dfoxfranke.lunaria))

* [xrdb/](./xrdb/) contains X resource files for theming terminals such as
  `xterm` and `rxvt`.

* [qterminal/](./qterminal/) contains themes for QTerminal-based terminals such
  as Konsole and LXQt.

* [gogh/](./gogh/) contains themes for terminals supported by Gogh, such as
  GNOME Terminal, XFCE4 Terminal, and iTerm.

* [css/](./css/) contains CSS files for using Lunaria in web design.

* [kitty/](./kitty/) contains the theme sources for the Kitty terminal emulator.

* [tmtheme/](./tmtheme/) contains the theme sources for applications that
  support .tmTheme file such as TextMate or Bat.

* [winterminal/](./winterminal/) contains the theme sources for the Windows
  Terminal.

## Development

In order to develop a color scheme / theme for another application that is not
available yet, you have to create a template file in the format that the
application supports.

This template file is used by `lunarize.py` and replaces every occurance of
`@<color_name>@` with the corresponding value.

As an example, you can take a look at [colors_template.md](./colors_template.md)
and see the results by looking at [colors_light.md](./colors_light.md),
[colors_dark.md](./colors_dark.md) or [colors_eclipse.md](./colors_eclipse.md).

These files also show you all available color names.

### Usage lunarize.py

```
usage: lunarize.py [-h] [--format {css_hex,css_rgb,decimal_rgb}] theme [input] [output]

Insert Lunaria colors into a template

positional arguments:
  theme                 JSON file defining theme colors
  input                 Template file (default: stdin)
  output                Output file (default: stdout)

options:
  -h, --help            show this help message and exit
  --format {css_hex,css_rgb,decimal_rgb}
                        How to format color codes
                        
                        A neutral gray would be formatted as follows:
                        
                        css_hex:      #808080
                        css_rgb:      rgb(50.00%,50.00%,50.00%)
                        decimal_rgb:  128,128,128
                        
                        The default is 'css_hex'
```

## License

Except as otherwise noted, the contents of this repo are Copyright &copy; Daniel
Fox Franke and licensed under the [Apache License, version 2.0](LICENSE.md).
However, the Lunaria color palette itself is not recognized as a copyrightable
work in most jurisdictions. To whatever extent the law recognizes any copyrights
to the following four files, I (Daniel Fox Franke) hereby waive those rights
worldwide and gift these files to the public domain:

* `lunaria-light.json` (SHA256: 56a3df482aeece28734904057f7bcdbe96f75dbb9f4992dc9b3ab86a1acb83b2)
* `lunaria-dark.json` (SHA256: a244706c77fc5441ccac3089d16b048b7165eede83e04fc27a80c55226aef71d)
* `lunaria-eclipse.json` (SHA256: 208c6406d4093acb1d881f4eea88db1e23e216cd6a38675774e8038c22895f23)
* `css/lunaria.css` (SHA256: 988b1b25d62ec3710558d5186bc9e1800cf2b973fdca883146d8c5d41f1546cc)

(Note: the last of these files is not checked into the repo; it is generated by
the build system using the first three as input).
