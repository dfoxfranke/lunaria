import sys
import os


colors = ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"]


def build_teststring(name, fg):
    text = [
        f'{name.ljust(15)}',
        f'\033[{str(fg)}m',
        'Normal',
        '\033[1mBold\033[22m',
        '\033[3mItalic\033[23m',
        '\033[4mUnderline\033[24m',
        '\033[21mDouble Underline\033[24m',
        '\033[0m',
        f'\033[{fg + 10}mBackground\033[0m'
    ]

    return ' '.join(text)


def print_colors():
    colors = [
        'Black', 'Red', 'Green', 'Yellow',
        'Blue', 'Magenta', 'Cyan', 'White'
    ]

    for i in range(0, 8):

        normal_fg = i + 30
        bright_fg = i + 90

        normal_name = colors[i]
        bright_name = f'Bright {colors[i]}'

        print(build_teststring(normal_name, normal_fg))
        print(build_teststring(bright_name, bright_fg))


def main():
    print_colors()
    print(os.linesep.join([
        os.linesep,
        'URL: https://lunaria.design',
        os.linesep,
        'MARK1    MARK2    MARK3',
        'Set the following in your kitty.conf and press F1 to see the colors:',
        'map f1 toggle_marker text 1 MARK1 2 MARK2 3 MARK3',
        os.linesep,
        'SELECTION'
    ]))

if __name__ == "__main__":
    main()
