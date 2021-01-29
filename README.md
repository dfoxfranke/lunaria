# Lunaria

Lunaria is a fam­ily of sooth­ing, moderate-​contrast color palettes
for ter­mi­nals, text ed­i­tors, and tech­ni­cal doc­u­men­ta­tion.
Lu­naria's col­ors were gen­er­ated al­go­rith­mi­cally, em­ploy­ing
the cut­ting edge of color sci­ence: the CAM16 color ap­pear­ance
model and its as­so­ci­ated uni­form color space and chro­matic
adap­ta­tion trans­form. Lu­naria in­cludes three dis­tinct
palettes:

Lu­naria in­cludes three dis­tinct palettes:

* The *Light* palette is for users who pre­fer to read dark text on
  a light back­ground. It is de­signed to pro­vide the best
  fac­sim­ile of ink-​on-paper that an LCD mon­i­tor can pos­si­bly
  achieve. Its col­ors are op­ti­mized for view­ing in the bright
  window-​lit con­di­tions typ­i­cal of 21st cen­tury of­fice
  build­ings, but hold up well in a broad range of con­di­tions.

* The *Dark* palette is for users who pre­fer light text on a dark
  back­ground. Its neu­tral col­ors are de­signed to give an
  im­pres­sion of a moon­lit night and are de­rived from ac­tual
  spec­tral data col­lected from the Fred Lawrence Whip­ple
  moun­tain­top as­tro­nom­i­cal ob­ser­va­tory. It is op­ti­mized
  for night­time view­ing under dim, warm LED il­lu­mi­na­tion.

* The *Eclipse* palette is al­most iden­ti­cal to the Dark palette,
  but op­ti­mized for the same brighter view­ing con­di­tions as the
  Light palette is. The most vis­i­ble dif­fer­ence is that the
  back­ground is darker as a re­sult of com­pen­sat­ing for
  in­creased view­ing flare (am­bi­ent light re­flected off the
  mon­i­tor sur­face).

## What's here

For a detailed, designer-focused introduction to Lunaria and how to
use it in your own work, see <https://lunaria.design>. All other
"official" Lunaria resources are here in this repo.

* The files [lunaria-light.json](./lunaria-light.json), [lunaria-dark.json](./lunaria-dark.json), and [lunaria-eclipse.json](./lunaria-eclipse.json)
   canonically define the respective color palettes. 

* [lunarize.py](./lunarize.py) is a script for substituting color definitions
  (provided by one of the above JSON files) into a template.

* [lunaria.ipynb](./lunaria.ipynb) is the Jupyter notebook which was used to generate
  Lunaria. Go here if you're interested in the gory mathematical
  details of how it was constructed.

* [vscode/](./vscode/) contains the sources of the Lunaria extension for Visual
  Studio Code.

* [xrdb/](./xrdb/) contains an X resource file for theming terminals such as
  `xterm` and `rxvt`.

* [qterminal/](./qterminal/) contains themes for QTerminal-based terminals such as
  Konsole and LXQt.

* [css/](./css/) contains CSS files for using Lunaria in web design.

## License

Except as otherwise noted, the contents of this repo are Copyright ©
Daniel Fox Franke and licensed under the [Apache License, version
2.0](LICENSE.md). However, the Lunaria color palette itself is not
recognized as a copyrightable work in most jurisdictions. To
whatever extent the law recognizes any copyrights to the following
four files, I (Daniel Fox Franke) hereby waive those rights
worldwide and gift these files to the public domain:

* `lunaria-light.json` (SHA256: 56a3df482aeece28734904057f7bcdbe96f75dbb9f4992dc9b3ab86a1acb83b2)
* `lunaria-dark.json` (SHA256: a244706c77fc5441ccac3089d16b048b7165eede83e04fc27a80c55226aef71d)
* `lunaria-eclipse.json` (SHA256: 208c6406d4093acb1d881f4eea88db1e23e216cd6a38675774e8038c22895f23)
* `css/lunaria.css` (SHA256: 988b1b25d62ec3710558d5186bc9e1800cf2b973fdca883146d8c5d41f1546cc)

(Note: the last of these files is not checked into the repo; it is
generated by the build system using the first three as input).