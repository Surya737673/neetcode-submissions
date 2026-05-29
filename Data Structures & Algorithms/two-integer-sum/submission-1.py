class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        l = len(nums)
        for i in range(l):
            compliment = target - nums[i]
            if compliment in dic:
                return [dic[compliment], i]
            
            dic[nums[i]] = i
        return []