import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x_coord = [x[0] for x in points]
        y_coord = [y[1] for y in points]
        dist_dict = []
        for i in range(len(points)):
            dist_dict.append([-sqrt(x_coord[i]**2 + y_coord[i]**2), [x_coord[i], y_coord[i]]])
        heap = []
        for i in range(len(points)):
            heapq.heappush(heap, dist_dict[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]