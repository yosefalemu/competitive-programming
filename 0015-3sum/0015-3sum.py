class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0  and nums[i] == nums[i - 1]:
                continue
            left_pt = i + 1
            right_pt = len(nums) - 1
            while left_pt < right_pt:
                curr = nums[i] + nums[left_pt] + nums[right_pt]
                if curr == 0:
                    ans.append((nums[i], nums[left_pt], nums[right_pt]))
                    left_pt += 1
                    right_pt -= 1
                    while left_pt < right_pt and nums[left_pt] == nums[left_pt - 1]:
                        left_pt += 1
                    while left_pt < right_pt and nums[right_pt] == nums[right_pt + 1]:
                        right_pt -= 1
                elif curr > 0:
                    right_pt -= 1
                else:
                    left_pt += 1
        return ans

                
        