def jump2(count: int, steps: [int]) -> [int]:
    n = len(steps)
    new_steps = [(steps[i], i) for i in range(n)]
    new_steps.sort()
    ans = []
    min_index_sum = float("inf")
    for i in range(n - 2):
        curr = new_steps[i][0]
        if i > 0 and new_steps[i][0] == new_steps[i - 1][0]:
            continue
        target = count - curr
        l = i + 1
        r = n - 1
        
        # 【剪枝】：
        thresh = (count - curr) / 2
        if new_steps[l][0] > thresh or new_steps[r][0] < thresh:
            break
            
        while l < r and l <= n - 1 and r >= i + 1:
            left = new_steps[l][0]
            right = new_steps[r][0]
            if left + right < target:
                l += 1
                while new_steps[l][0] == new_steps[l - 1][0]:   
                    l += 1
            elif left + right > target:
                r -= 1
                while new_steps[r][0] == new_steps[r + 1][0]:  
                    r -= 1
            elif left + right == target:
                # 【在这里剪枝】  # 找index之和最小的组，所以r先左移，然后l右移
                while l < r - 1 and new_steps[r][0] == new_steps[r - 1][0]:
                    r -= 1
                
                if min_index_sum > new_steps[i][1] + new_steps[l][1] + new_steps[r][1]:
                    min_index_sum = new_steps[i][1] + new_steps[l][1] + new_steps[r][1]
                    tmp = [new_steps[i], new_steps[l], new_steps[r]]
                    tmp.sort(key = lambda x: x[1])
                    ans = [x[0] for x in tmp]
                    
                # 【剪枝】
                while l < r - 1 and new_steps[l][0] == new_steps[l + 1][0]:
                    l += 1
                l += 1
                r -= 1
    return ans

# count = int(input())
# steps = list(map(int, input().split()))
count = 9
steps = [1, 4, 5, 2, 0, 2]
print(jump2(count, steps))
count = 9
steps = [1, 5, 2, 0, 2, 4]
print(jump2(count, steps))
count = 12
steps = [-1, 2, 4, 9]
print(jump2(count, steps))