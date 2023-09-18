ui_width = 30

def line(dots=None):
    if dots is True:
        print("*"* ui_width)
    else:
        print("-"* ui_width)

def header(text):
    print("|" + text.center(ui_width - 2) + "|")

def echo(text):
    print("| " + text)

def prompt(text):
    cmd = input(f"| {text} > ")
    return cmd

