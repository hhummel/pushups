def validate(s):

    stack = []
    dict = {
        ")": "(", 
        "]": "[", 
        "}": "{", 
    }

    for c in s:
        if c in dict.values():
            stack.append(c)
        elif c in dict.keys() and (not stack or dict[c] != stack.pop()):
            return False

    return len(stack) == 0

if __name__ == "__main__":

    print(validate("{(9 * 9) + [9 + 7]}"))
