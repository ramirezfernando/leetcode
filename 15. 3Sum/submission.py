class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):

            # we don't want duplicate triplets in our output
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # we don't for duplicate triplets while still making sure j < k
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
        return output