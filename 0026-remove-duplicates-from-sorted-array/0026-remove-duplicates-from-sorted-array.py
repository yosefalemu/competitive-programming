class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_pt = 0
        for fast_pt in range(len(nums)):
            if fast_pt > 0 and nums[slow_pt] != nums[fast_pt]:
                slow_pt += 1
                nums[slow_pt] = nums[fast_pt]
        return slow_pt + 1
        