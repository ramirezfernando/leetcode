class Solution:
    def numRescueBoats(self, people, limit):

        people.sort()
        boats = 0
        l, r = 0, len(people) - 1

        if len(people) == 1:
            return 1

        while l < r:
            # [2 ... 5], limit = 6
            if people[l] + people[r] > limit:
                boats += 1
                r -= 1
            # [1 ... 5], limit = 6
            else:
                l += 1
                r -= 1
                boats += 1
            # one person left
            if l == r:
                boats += 1

        return boats