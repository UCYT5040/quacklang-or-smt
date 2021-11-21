# Quacklang Or SMT

import re

def err(text, warning=True):
    warn = "\033[93m"
    fail = "\033[91m"
    reset = "\033[0m"
    if warning: print(f"{warn}{text}{reset}")
    else: print(f"{fail}{text}{reset}")

def split_into_list(code): return [line.strip() for line in code.split(";") if line != ""]

def run_string(code):
    lines = split_into_list(code) # Get a list of lines.
    # Iterate over each line.
    for line_num in range(len(lines)):
        line = lines[line]
        # We use regex to check syntax of each line.
        if not re.match(".+\(.*\)", line): err(f"Line {line_num}: This line does not appear to be valid. Check that it contains a function.")
        # ^ Error message is sent if there isn't a function to run.
        # Now we need to find the function name.
        function = line.split("(")[0]
        ...