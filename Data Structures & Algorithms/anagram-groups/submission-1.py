class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for s in strs:
            x = "".join(sorted(s))
            if x in result_dict:
                result_dict[x].append(s)
            else:
                result_dict[x] = [s]
        return [result_dict[x] for x in result_dict.keys()]
            