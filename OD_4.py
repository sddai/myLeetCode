from collections import deque
def max_period(s, M, T, P):
    n = len(s)
    i = 0
    cycle = 0
    # recovered = 0
    q = deque()
    fault = 0
    while i < n:
        # if cycle >= M and fault >= T:
        if cycle <= M:
            if fault == T:
                recovered = 0
                while recovered < P and i < n:
                    if isValid(i):
                        recovered += 1
                    else:
                        recovered = 0
                    i += 1
                cycle = 0
                fault = 0
                continue
            if cycle == M:
                cycle = 0
                fault = 0
                continue
#             if isValid(i):
#                 recovered += 1
#             if recovered >= P :
#                 cycle = 0
#                 fault = 0
#             i += 1
#             continue
            
        if isValid(i):
            q.append(i)
            # cycle += 1
            # i += 1
        else:
            fault += 1
            if q:
                s[i] = s[q[-1]]
                q.append(i)
            # cycle += 1
            
            # i += 1
        cycle += 1
        i += 1
        
    tmp = 1
    ans = 0
    lastIndex = q.pop()
    while q:
        if q[-1] == lastIndex - 1:
            tmp += 1
            lastIndex = q.pop()
        else:    
            ans = max(ans, tmp)
            tmp = 1
            lastIndex = q.pop()
    return tmp if ans == 0 else ans
        
    
def isValid(i):
    if s[i] <= 0:
        return False
    elif i > 0 and s[i] < s[i - 1]:
        return False
    elif i > 0 and s[i] - s[i - 1] >= 10:
        return False
    else:
        return True


# M, T, P = map(int, input().split())
# s = list(map(int, input().split()))
M, T, P = [10, 6, 3]
s = [-1, 1, 2, 3, 100, 13, 9, 10]
a = max_period(s, M, T, P)
print(a)


# def max_period(s, M, T, P):
    
#     n = len(s)
#     fault_count = 0
#     start = 0
#     end = 0
#     restore_start = 0
#     restore_end = 0
#     max_period = 0
#     curr_period = 0
#     fault_flag = [0] * n
#     for i in range(n):
#         # curr = s[i]
#         end = i
#         if s[i] <= 0:
#             fault_flag[i] = True
#             fault_count += 1
#         elif i > 0 and s[i] < s[i- 1]:
#             fault_flag[i] = True
#             s[i] = s[i - 1]
#             fault_count += 1
#         elif i > 0 and s[i] - s[i - 1] >= 10:
#             fault_flag[i] = True
#             s[i] = s[i - 1]
#             fault_count += 1
#         else:
#             curr_period += 1
        
#         if end - start + 1 <= fault_window_size and fault_count >= fault_thresh:
#             # fault_flag = True
#             restore_start = i + 1
#             restore_end = i + 1
#         if end - start + 1 > fault_window_size:
#             if fault_flag[start] == 1:
#                 fault_count -= 1
#             start += 1
        
#         # if fault_flag == True: