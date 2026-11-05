import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            temp = []

            for i in range(n + 1):
                if heap:
                    count = -heapq.heappop(heap)

                    if count > 1:
                        temp.append(-(count - 1))

                time += 1

                if not heap and not temp:
                    break

            for x in temp:
                heapq.heappush(heap, x)

        return time