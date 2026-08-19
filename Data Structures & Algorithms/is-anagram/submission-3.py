class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                letter_freq[s[i]] = letter_freq.get(s[i], 0) + 1
                letter_freq[t[i]] = letter_freq.get(t[i],0) - 1
            print(letter_freq)
        return all(v==0 for v in letter_freq.values())



