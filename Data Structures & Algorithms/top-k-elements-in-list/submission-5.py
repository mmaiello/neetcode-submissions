import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numfreq = {}
        for num in nums:
            if num in numfreq:
                numfreq[num] += 1
            else:
                numfreq[num] = 1

        heap = []
        for num,freq in numfreq.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num[1] for num in heap]