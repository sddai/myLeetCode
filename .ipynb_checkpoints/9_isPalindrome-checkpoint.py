def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    x = str(x)
    start = 0
    end = len(x) - 1
    while start <= end:
        if x[start] ==  x[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


print(  isPalindrome(121211)  )