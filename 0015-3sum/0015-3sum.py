class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            left_pt = i + 1
            right_pt = len(nums) - 1
            while left_pt < right_pt:
                curr = nums[i] + nums[left_pt] + nums[right_pt]
                if curr == 0:
                    ans.add((nums[i], nums[left_pt], nums[right_pt]))
                    left_pt += 1
                    right_pt -= 1
                elif curr > 0:
                    right_pt -= 1
                else:
                    left_pt += 1
        main_ans = []
        for a in ans:
            main_ans.append(list(a))
        return main_ans

                
        