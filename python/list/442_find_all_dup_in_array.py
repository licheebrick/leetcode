class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup_list = list()
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup_list.append(abs(num))
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]
        return dup_list
