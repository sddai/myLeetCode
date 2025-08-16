class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def find(nums, k):
            n = len(nums)
            stack = []
            drop = n - k
            for i in nums:
                while drop > 0 and stack and stack[-1] < i:   # 保留k个元素，则需要删掉n-k个元素
                    stack.pop()
                    drop -= 1
                stack.append(i)
                # k -= 1
            # print(nums[:k])
            return stack[:k]   # 注意这里返回的不是nums[:k]，而是stack[:k]
        def merge(nums1, nums2):   # merge([6, 7], [6, 0, 4]), 用双指针会返回66704而不是67604
                                    # 这是由于不能只判断第一个数字，而是应该判断整个序列（67>60）
                                    # (解决方案)另写一个函数判断大小，或者list直接用大于号比较
            ans = []
            while nums1 or nums2:
                bigger = max(nums1, nums2)
                ans.append(bigger.pop(0))
            # n1 = len(nums1)
            # n2 = len(nums2)
            # p1 = 0
            # p2 = 0
            # ans = []
            # while p1 <= n1 - 1 and p2 <= n2 - 1:
            #     if nums1[p1] > nums2[p2]:
            #         ans.append(nums1[p1])
            #         p1 += 1
            #     else:
            #         ans.append(nums2[p2])
            #         p2 += 1
            # if p1 <= n1 - 1:
            #     while p1 <= n1 - 1:
            #         ans.append(nums1[p1])
            #         p1 += 1
            # if p2 <= n2 -1:
            #     while p2 <= n2 - 1:
            #         ans.append(nums2[p2])
            #         p2 += 1
            return ans
        
        res = []
        n = len(nums1)
        m = len(nums2)
        for i in range(k + 1):
            k1 = i
            k2 = k - i
            if k1 <= n and k2 <= m:
                res.append(merge(find(nums1, k1), find(nums2, k2)))
                print(find(nums1, k1))
                print(find(nums2, k2))
                print(merge(find(nums1, k1), find(nums2, k2)))
                print("---")
        
        return max(res)

