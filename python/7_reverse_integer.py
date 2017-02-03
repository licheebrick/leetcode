class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -int("".join(str(x)[1:][::-1]))
        else:
            return int(str(x)[::-1])
