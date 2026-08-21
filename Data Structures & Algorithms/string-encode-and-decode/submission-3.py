class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs: 
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        left = 0 
        res = []
        while left < len(s):
            j = left
            #At the beginning, left corresponds to the length of the first word. After this first length, there is a # and the word follows. 
            while s[j] != "#":
                j += 1
            #Now j is at the position of the # preceeding the word.
            length = int(s[left:j])
            res.append(s[j+1 :j + 1 + length])
            left = j + 1 + length #This is the length of the next word.
        return res