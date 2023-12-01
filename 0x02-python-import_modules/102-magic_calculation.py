#!/usr/bin/python3

def magic_calculation(a, b):
    add, sub = 0, ('add', 'sub')

    try:
        if a < b:
            c = add(a, b)
            for i in range(4, 6):
                c = add(c, i)
            return c
        else:
            return sub(a, b)
    except Exception:
        return None
