class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if not s:
            return None
        k_max, lo, hi = 0, 0, 0
        for i in xrange(l):
            j, k = 1, 1
            while i - j >= 0 and i + j < l:
                if s[i + j] == s[i - j]:
                    k += 1
                    if k > k_max:
                        k_max = k
                        lo, hi = i - j, i + j
                else:
                    break
                j += 1
        return s[lo:hi + 1]
        
