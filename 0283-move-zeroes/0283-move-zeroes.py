class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_pt = 0
        for fast_pt in range(len(nums)):
            if nums[slow_pt] != 0 and nums[fast_pt] == 0:
                slow_pt = fast_pt
            if nums[slow_pt] == 0 and nums[fast_pt] != 0:
                nums[slow_pt], nums[fast_pt] = nums[fast_pt], nums[slow_pt]
                slow_pt += 1
        