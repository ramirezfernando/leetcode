import heapq

class Solution:
    def topKFrequent(self, nums, k):
        
        # get frequency of each number in nums (num : frequency) using hashmap
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # make heap of tuples (frequency, num) to only contain k most frequent nums
        heap = []
        for num, freq in freq.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))

        # extract the num from tuples by adding them to ans list
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans

        '''
        Time complexity: O(nlogk)
        Space complexity: O(n)
        '''