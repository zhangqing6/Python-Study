class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        # 总和奇数，不可平分
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # 倒序，防止重复选同一个元素
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            # 提前剪枝，找到直接返回
            if dp[target]:
                return True
        return dp[target]
