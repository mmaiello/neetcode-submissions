class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs: 
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0 
        while left < len(s):
            j = left
            while s[j] != "#":
                j += 1
            length = int(s[left:j])
            res.append(s[j +1 : j + 1 + length])
            left = j + 1 + length
        return res