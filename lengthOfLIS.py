class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n  # 每个数字自己最少长度是1
        
        for i in range(n):
            # 检查 i 前面所有的数字 j
            for j in range(i):
                # 如果前面数字 < 当前数字，可以接上去
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
