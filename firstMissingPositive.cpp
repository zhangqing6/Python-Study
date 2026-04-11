class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 第一步：遍历数组，将每个正确的数放到对应位置
        for i in range(n):
            # 只有当数字在[1,n]范围内，且不在正确位置时，才交换
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交换 nums[i] 和 nums[nums[i]-1]
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # 第二步：遍历找第一个位置不匹配的数
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 所有数都匹配，返回n+1
        return n + 1
