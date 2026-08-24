class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dict = {}
        res = []
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            for j in range(len(nums)):
                if -nums[i] -nums[j] in nums_dict and i != j and j != nums_dict[-nums[i]- nums[j]] and i != nums_dict[-nums[i] - nums[j]] and sorted([nums[i],nums[j],-nums[i] - nums[j]]) not in res:
                    res.append(sorted([nums[i],nums[j],-nums[i] - nums[j]]))
        
        return res