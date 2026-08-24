class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        ans = 1
        res = 1
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                ans += 1
                res = max(res,ans)
            elif nums[i+1] - nums[i] == 0:
                ans += 0
            else:
                ans = 1
        return res