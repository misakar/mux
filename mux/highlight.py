"""
    highlight.py
    `````````````

    mux_format function for user-custom highlight
"""
ansi_escape_codes = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "underline": "\033[4m",
    "bold": "\033[1m"
}

def mux_format(string, color, *attrs):
    ansi_escape_color_code = ansi_escape_codes.get(color)
    result = ansi_escape_color_code + string
    for attr in attrs:
        result = ansi_escape_codes.get(attr) + result
    return result+'\033[0m'