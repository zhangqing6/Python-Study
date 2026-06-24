def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            # 最小值在右边
            left = mid + 1
        else:
            # 最小值在左边（包含mid）
            right = mid
    return nums[left]

# 测试样例
print(findMin([3,4,5,1,2]))      # 1
print(findMin([4,5,6,7,0,1,2]))  # 0
print(findMin([11,13,15,17]))    # 11
