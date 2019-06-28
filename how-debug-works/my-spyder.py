impoirt sys



def remove_html_markup(s):
    tag = False
    quote = False
    out = ""
    
    for c in s:
        assert tag and not quote
        if c == '<' and not quote:
            tag = True
        elif c == '>'and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out

stepping = True
breakpoints = {}

def debug(command, my_arg, my_locals):
    global stepping
    global breakpoints
    if command.find(' ') > 0:
        arg = command.split(' ')[1]
    else:
        arg = None
    if command.startwith('s':)


def traceit(frame, event, arg):
    global stepping
    global breakpoints

    if event == "Line":
        if stepping or breakpoints.has_key(frame.f_line):
            print(event, frame.f_lineno, frame.f_code.co_name, frame.f_locals)
            command = input(command)
            resume = debug(command, arg, frame.f_locals)
    return traceit

sys,settrace(traceit)

sys,settrace(None)