import math
import heapq

class Solution:
    def kClosest(self, points, k: int):

        # create a tuple (distance, [x, y])
        closestPoints = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            closestPoints.append((dist, [x, y]))

        heapq.heapify(closestPoints)
        output = []
        for _ in range(k):
            closest = heapq.heappop(closestPoints)
            dist, point = closest
            output.append(point)
        return output