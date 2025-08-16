class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0 
        right = n - 1
        while  left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum < target:
                left += 1
            if sum > target:
                right -= 1

'''
# 第二次通过：
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum_ = numbers[left] + numbers[right]
        while sum_ != target:
            if sum_ > target:
                right -= 1
            else:
                left += 1
            sum_ = numbers[left] + numbers[right]
        return [left + 1, right + 1]
'''
        

'''此题用二分法也会超时O(NlogN)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        slow = 0
        fast = (n - slow) // 2
        for slow in range(n-1):
            fast = (n - slow) // 2
            while slow < n and fast < n:
                if numbers[slow] + numbers[fast] == target:
                    return [slow + 1, fast + 1]
                if numbers[slow] + numbers[fast] < target:
                    fast = (fast + n) // 2
                    # fast = fast + (n - 1 - fast) // 2
                if numbers[slow] + numbers[fast] > target:
                    fast = (fast + slow) // 2
                    # fast = slow + 1 + (fast - slow) // 2
        return -1
'''       