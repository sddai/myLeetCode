def concatinate(s, t):
    left_line = s[-1] == "/"
    right_line = t[0] == "/"
    if left_line and right_line:
        return s[:] + t[1:]
    elif left_line or right_line:
        return s[:] + t[:]
    else:
        return s[:] + "/" + t[:]

s = "/acm"
t = "/bb"
print(concatinate(s, t))
s = "/acm/"
t = "/bcd"
print(concatinate(s, t))
s = "/acm"
t = "bb"
print(concatinate(s, t))