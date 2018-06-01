class Solution:
    # nums为有序数组 可能包含重复元素 和为target result存放结果的list
    def twoSum(self, nums, l, r, target, result, first, second):  # [l...r]
        # 利用对撞指针来进行
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                result.append([first, second, nums[l], nums[r]])
                l += 1
                r -= 1
                # 避免重复元素
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1

            elif sum > target:
                r -= 1
            else:
                l += 1
        return result

    def threeSum(self, nums, l, r, target, result, first):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(l, r - 1):
            if i > l and nums[i] == nums[i - 1]:  # 去除重复元素
                continue
            val = target - nums[i]
            result = self.twoSum(nums, i + 1, r, val, result, first, nums[i])
        return result

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 思想 转化为三数和问题
        result = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            val = target - nums[i]
            result = self.threeSum(nums, i + 1, n - 1, val, result, nums[i])
        return result

print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
from collections import Counter