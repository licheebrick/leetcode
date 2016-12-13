class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = dict()
        for index, num in enumerate(nums):
            if hash.has_key(num):
                return [hash[num], index]
            hash[target - num] = index
        return None
