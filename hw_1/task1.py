def balanced_brackets(st):
    d = dict(zip('({[', ')}]'))
    stack = []
    for char in st:
        if char in d.keys():
            stack.append(d[char])
        elif char in d.values():
            if not stack or char != stack.pop():
                return False
    return not stack
