# Quacklang Or SMT

import re, json, os


def err(text, warning=False):
    reset = "\033[0m"
    if warning:
        print(f'\x1b[93m{text}{reset}')
    else:
        print(f'\x1b[91m{text}{reset}')
        exit(1)


def split_into_list(code, sep=";"): return [
    line.strip() for line in code.split(sep) if line != ""]


# This needs its own way of evaluating, and poses a security risk.
def value_of(code):
    #return eval(code)
    return code # For some reason it seems to be already evaluated, investigating.


def run_func(function, line, line_num, function_name):
    if function["using"] == "python_exec":
        # We need to get arguments.
        if len(function["arguments"]) != 0:
            get_args(line, function, line_num, function_name)
        # If the function does not need any arguments, just execute it.
        exec(function["run"])
    elif function["using"] == "python_eval":
        # We need to get arguments.
        if len(function["arguments"]) != 0:
            get_args(line, function, line_num, function_name)
        # If the function does not need any arguments, just execute it.
        eval(function["run"])
    elif function["using"] == "quacklangorsmt":
        if len(function["arguments"]) != 0:
            get_args(line, function, line_num, function_name)
        # If the function does not need any arguments, just execute it.
        run_string(function["run"])


def get_args(line, function, line_num, function_name):
    args = [value_of(arg) for arg in split_into_list(
        re.search(".*?\((.*)\)", line).group(1),
        ",")]
    if len(args) != len(function["arguments"]):
        err(
            f"Line {line_num}: Function: {function_name}: Found {len(args)} arguments, expected {len(function['arguments'])}.")
    for arg_num in range(len(function["arguments"])):
        arg = function["arguments"][arg_num]
        function["run"] = function["run"].replace(f"!{arg}!", args[arg_num])


def run_string(code):
    builtins = json.loads(
        '{"name":"Builtins","author":"UCYT5040","functions":{"quack":{"using":"python_exec","arguments":["obj_to_print"],"run":"print(str(!obj_to_print!))"}}}')
    functions = builtins['functions']
    lines = split_into_list(code)  # Get a list of lines.
    # Iterate over each line.
    for line_num in range(len(lines)):
        line = lines[line_num]
        line_num += 1
        # We use regex to check syntax of each line.
        if not re.match(".+\(.*\)", line):
            err(f"Line {line_num}: This line does not appear to be valid. Check that it contains a function.")
        # ^ Error message is sent if there isn't a function to run.
        # Now we need to find the function name.
        function_name = line.split("(")[0]
        # Check for it in functions
        if function_name not in functions:
            err(f"Line {line_num}: No function named {function_name}. Did you import {function_name}?")
        # If it is a function we need to find the code it runs.
        function = functions[function_name]
        if "using" not in function:
            err(f"Line {line_num}: Function: {function_name} does not contain a proper run type.")
        if "run" not in function:
            err(f"Line {line_num}: Function: {function_name} does not contain run code.")
        # The function specifies it wants to be ran as Python.
        run_func(function, line, line_num, function_name)
