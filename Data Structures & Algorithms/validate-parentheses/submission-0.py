class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {']': '[', '}': '{', ')': '('}
        heap = []
        for i in range(len(s)):
            if s[i] not in closeToOpen:
                heap.append(s[i])
            else:
                if not heap:
                    return False
                else:
                    popped = heap.pop()
                    if popped != closeToOpen[s[i]]:
                        return False
        return not heap

        