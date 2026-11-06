# stack
def decode(s):
    stack = [""]

    for ch in s:
        if ch == "(":
            # male a top level
            stack.append("")              
        elif ch == ")":
            # remove the top level, in a reversed version
            inner = stack.pop()[::-1]  
            # add the reversed top level to the level under it, acting as a new top 
            stack[-1] += inner       
        else:
            # else add the letter to the current top
            stack[-1] += ch

    return stack[0]
