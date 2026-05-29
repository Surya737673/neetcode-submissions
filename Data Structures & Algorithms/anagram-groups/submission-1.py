class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for ch in strs:
            sorted_char = ''.join(sorted(ch))
            if sorted_char not in dic:
                dic[sorted_char] = []
            
            dic[sorted_char].append(ch)
        return list(dic.values())
