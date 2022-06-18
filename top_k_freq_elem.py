"""
Simple min heap logic if the heap length becomes greater than k then keep on popping.

"""

from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        counts = Counter(nums)
        heapify(pq)
         
        for i, j in dict(counts).items():
            heappush(pq, (j, i))
            if len(pq) > k:
                heappop(pq)
            
        return [ j for _, j in pq ]
        