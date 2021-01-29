#!/usr/bin/env bash

# ====================CONFIG THIS =============================== #
export COLOR_01="@black@"           # Black
export COLOR_02="@termLowRed@"           # Red
export COLOR_03="@termLowGreen@"           # Green
export COLOR_04="@termLowYellow@"           # Yellow
export COLOR_05="@termLowViolet@"           # Blue
export COLOR_06="@termLowMagenta@"           # Magenta
export COLOR_07="@termLowBlue@"           # Cyan
export COLOR_08="@lightGray@"           # Light gray

export COLOR_09="@darkGray@"           # Dark gray
export COLOR_10="@termHighRed@"           # Light Red
export COLOR_11="@termHighGreen@"           # Light Green
export COLOR_12="@termHighYellow@"           # Light Yellow
export COLOR_13="@termHighViolet@"           # Light Blue
export COLOR_14="@termHighMagenta@"           # Light Magenta
export COLOR_15="@termHighBlue@"           # Light Cyan
export COLOR_16="@white@"           # White

export BACKGROUND_COLOR="@bg@"   # Background Color
export FOREGROUND_COLOR="@fg@"   # Foreground Color (text)
export CURSOR_COLOR="$FOREGROUND_COLOR" # Cursor color
export PROFILE_NAME="@_name@"
# =============================================================== #







# =============================================================== #
# | Apply Colors
# ===============================================================|#
SCRIPT_PATH="${SCRIPT_PATH:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
PARENT_PATH="$(dirname "${SCRIPT_PATH}")"

# Allow developer to change url to forked url for easier testing
# IMPORTANT: Make sure you export this variable if your main shell is not bash
BASE_URL=${BASE_URL:-"https://raw.githubusercontent.com/Mayccoll/Gogh/master"}


if [[ -e "${PARENT_PATH}/apply-colors.sh" ]]; then
  bash "${PARENT_PATH}/apply-colors.sh"
else
  if [[ "$(uname)" = "Darwin" ]]; then
    # OSX ships with curl and ancient bash
    bash -c "$(curl -so- "${BASE_URL}/apply-colors.sh")"
  else
    # Linux ships with wget
    bash -c "$(wget -qO- "${BASE_URL}/apply-colors.sh")"
  fi
fi
