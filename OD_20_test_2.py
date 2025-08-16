def parse_string(s):
    isOpen = False
    main_chars = []
    eq_chars = []
    tmp = []
    for c in s:
        if c == '(':
            isOpen = True
            continue
        if c == ')':
            isOpen = False
            if tmp: 
                eq_chars.append(set(tmp))
                tmp = []
            continue
        if isOpen:
            tmp.append(c)
        else:
            main_chars.append(c)
    return main_chars, eq_chars

def merge_eq_chars(eq_chars):
    i = 0
    while i < len(eq_chars):
        merged = False
        for j in range(len(eq_chars)):
            if i == j:
                continue
            if eq_chars[i] & eq_chars[j] or {char.lower() for char in eq_chars[i]} & {char.lower() for char in eq_chars[j]}:
                eq_chars[i] = eq_chars[i].union(eq_chars[j])
                eq_chars.pop(j)
                merged = True
                break
        if not merged:
            i += 1
    return eq_chars

def replace_main_chars(main_chars, eq_chars):
    replace_dict = {}
    for chars in eq_chars:
        if chars:  
            min_char = min(chars, key=lambda x: (x.lower(), x))
            for char in chars:
                replace_dict[char] = min_char
                replace_dict[char.lower()] = min_char
                replace_dict[char.upper()] = min_char

    result = ''.join([replace_dict.get(c, c) for c in main_chars])
    return result if result else '0'

def simplify_string(s):
    main_chars, eq_chars = parse_string(s)
    eq_chars = merge_eq_chars(eq_chars)
    return replace_main_chars(main_chars, eq_chars)

input_str = "(abd)demand(fb)()for"
print(simplify_string(input_str))

