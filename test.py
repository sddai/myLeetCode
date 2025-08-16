from typing import List
def nextGreaterElements(  nums: List[int]) -> List[int]:
    stack = [0]
    n = len(nums)
    i = 1
    cnt = 1
    res = [-1] * n
    while cnt <= 2 * n - 3:
        if i == n:
            i = 0
        if stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]
        else:
            stack.append(i)
        i +=1 
        cnt += 1
    return res


print(nextGreaterElements([1,2,3,4,3]))