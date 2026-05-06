class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_pt = 0
        count = 1
        for fast_pt in range(1, len(nums)):
            if nums[slow_pt] == nums[fast_pt]:
                count += 1
            else:
                count = 1
            if count < 3:
                slow_pt += 1
                nums[slow_pt] = nums[fast_pt]
        return slow_pt + 1


        