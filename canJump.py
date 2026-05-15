class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0  # 记录当前能跳到的最远下标
        n = len(nums)
        
        for i in range(n):
            # 如果当前位置都到不了，直接返回 False
            if i > max_reach:
                return False
            
            # 更新能跳到的最远位置
            max_reach = max(max_reach, i + nums[i])
            
            # 如果最远位置已经能到达终点，提前返回 True
            if max_reach >= n - 1:
                return True
        
        return True
