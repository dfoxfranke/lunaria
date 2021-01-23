#!/bin/sh
sed -e 's/#0d1117/___XBLACK___/g' \
    -e 's/#2d3136/___BLACK___/g' \
    -e 's/#565a60/___DARKGRAY___/g' \
    -e 's/#b9b6af/___LIGHTGRAY___/g' \
    -e 's/#ebe8e0/___WHITE___/g' \
    -e 's/#faf6ef/___XWHITE___/g' \
    -e 's/#043255/___BLUE___/g' \
    -e 's/#fbe6b8/___YELLOW___/g' \
    -e 's/___XBLACK___/#faf6ef/g' \
    -e 's/___BLACK___/#ebe8e0/g' \
    -e 's/___DARKGRAY___/#b9b6af/g' \
    -e 's/___LIGHTGRAY___/#565a60/g' \
    -e 's/___WHITE___/#2d3136/g' \
    -e 's/___XWHITE___/#0d1117/g' \
    -e 's/___YELLOW___/#043255/g' \
    -e 's/___BLUE___/#fbe6b8/g'