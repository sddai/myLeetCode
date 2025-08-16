def solution(n, alist):
    # alist.sort(key = lambda x: (x[0], -x[1]))
    alist.sort()
    stack = [alist[0]]
    for i in range(1, n):
        curr = alist[i]
        top = stack[-1] if stack else None
        while True:
            if not top:  #如果栈为空
                stack.append(curr)
                break   
            top_start, top_end = top
            curr_start, curr_end = curr
            if curr_end <= top_start:  # curr在top左侧且无重叠
                break
            elif curr_start <= top_start and curr_end <= top_end:  # curr 在 top 的左侧，有重叠
                break
            elif curr_start <= top_start and curr_end > top_end:   # curr完全覆盖top
                stack.pop()  #当前区间完全覆栈顶区间
            elif curr_start > top_start and curr_end > top_end: # curr在top右侧有重叠 
                stack.append([top_end, curr_end])
                # stack.append(curr)
                break
            else:
                stack.append(curr)  # curr在top右侧且无重叠
            top = stack[-1] if stack else None
    return len(stack)
                
ans = solution(3, [[1, 4], [2, 5], [3, 6]])
print(ans)             
                
                
    
#     count = 1
#     farthest = alist[0][1]
#     # print(alist)
#     i = 1
#     select = 0
#     while i < n:
#         start, end = alist[i]
#         new_far = farthest
#         # for next_start, next_end in
#         while start <= farthest:
#             new_far = max(new_far, end)
#             select = i if new_far == end else select
#             i += 1
#             if start, end = alist[i]
        
#         # if new_far != farthest:
#             # count += 1
        
#         i += 1
    
    
    # for start, end in alist:
    #     # farthest = max(farthest, end)
    #     if farthest != max(farthest, end):
    #         farthest = end
    #         count += 1
    #     if 
        # if farthest != max(farthest, end):
        #     count += 1
        #     farthest = end
        
        # elif start > farthest:
        #     count += 1
        #     farthest = end
    # return count 

