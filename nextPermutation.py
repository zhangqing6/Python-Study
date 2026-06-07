class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1. 从后往前找第一个 升序 对 nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # 如果找到了 i（不是最大排列）
        if i >= 0:
            # 2. 从后往前找第一个比 nums[i] 大的数
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交换 i 和 j
            nums[i], nums[j] = nums[j], nums[i]
        
        # 3. 反转 i 后面的所有元素（如果i=-1，反转整个数组）
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
