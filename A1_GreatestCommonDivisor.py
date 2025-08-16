def GCD(a: int, b: int)->int:
    while b != 0:
        r = a % b
        a = b
        b = r
        print("a=", a, "b=", b, "r=", r)
    return a

print(GCD(12, 15))