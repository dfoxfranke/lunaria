# TmTheme

Theme for applications that support .tmTheme files. Some of them are:

- [TextMate](https://macromates.com)
- [Bat](https://github.com/sharkdp/bat)

It should also work with [Sublime Text](https://www.sublimetext.com), but the
support for .tmTheme files is considered as lagacy in Sublime Text. Please refer
to the [docs](https://www.sublimetext.com/docs/color_schemes_tmtheme.html) for
more information.

## Usage

Run `make` and copy the generated `.tmTheme` file of your choice to the desired
directory. Some applications will also let you import the theme file via their
GUI.

## Development

[Here](https://www.sublimetext.com/docs/scope_naming.html) you can find some
help regarding the scope names in case you want to improve this theme.

To test your changes against a specific language, you can use the files with the
prefix `syntax_test_` in
[this repository](https://github.com/sublimehq/Packages).
