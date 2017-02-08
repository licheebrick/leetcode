class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len, maxlen = 0, 0
        for num in nums:
            if num:
                len+=1
                maxlen = max(len, maxlen)
            else:
                len = 0
        return maxlen
