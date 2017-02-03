class Solution(object):
    # longest common substring
    def longestPalindrome1(self, s):
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

    # expand from center:
    def longestPalindrome2(self, s):
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
        for i in xrange(l - 1):
            j, k = 0, 1
            while i - j >= 0 and i + j + 1 < l:
                if s[i - j] == s[i + j + 1]:
                    k += 1
                    if k > k_max:
                        k_max = k
                        lo, hi = i - j, i + j + 1
                else:
                    break
                j += 1
        return s[lo:hi + 1]
