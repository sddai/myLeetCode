from collections import defaultdict
def process(line):
    col_to_content = defaultdict(str)
    i = 0
    while i < len(line) and line[i] != ",":
        col_to_content["A"] += line[i]
    # col_to_content["A"] = 
    j = 1
    while i < len(line):
        while line[i] != ",":
            col_to_content[chr(ord("A") + j)] += line[i]
            i += 1
        j += 1
        i += 1
    for col, content in col_to_content:
        # for i in len(content):
        i = 0
        while i < len(content): 
            tmp = ""
            if c == "<":
                i += 1
                tmp += content[i]
                i += 2
                continue
            # elif c == ">":
                # pass
            else:
                tmp += content[i]
            i += 1
        col_to_content[col] = tmp
    i = 0
    res = ""
    # for c in line:
    while i < len(line):
        if line[i] == "<":
            i += 1
            res += col_to_content[line[i]]
            i += 1
        else:
            res += line[i]
            i += 1
        # if line[i] == ">":
    return res


line = "<B>12,10"
print(process(line))