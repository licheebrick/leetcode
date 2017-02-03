class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = ""
        l = len(s)
        if not l:
            return zigzag
        if numRows is 1:
            return s
        base = 2 * numRows - 2
        rounds = int(math.ceil(l / (base * 1.0)))
        #print rounds, l
        for i in xrange(numRows):
            for j in xrange(rounds):
                #print
                #print i, j
                if j * base + i < l:
                    #print j * base + i
                    zigzag += s[j * base + i]
                x = numRows - 1 - i
                if (0 < x < numRows - 1) and (j * base + numRows + x - 1 < l):
                    #print j * base + numRows + x - 1
                    zigzag += s[j * base + numRows + x - 1]
        #print len(zigzag)
        return zigzag
