def min_steps(n):
    r = n % 3
    if r  == 0:
        return n // 3
    if r == 1:
        # return (n - 1) // 3 + 2
        return (n - 4) // 3 + 2
    if r == 2:
        return (n - 2) // 3 + 1
    
n = int(input())
print(min_steps(n))