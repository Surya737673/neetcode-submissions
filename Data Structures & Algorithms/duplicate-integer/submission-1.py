class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num in dict and dict[num] >=1:
                return True
            dict[num] = dict.get(num, 0) + 1

        return False