class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) is 0:
            return 0
        time_sum = 0
        for index in range(0, len(timeSeries) - 1):
            time_itv = timeSeries[index + 1] - timeSeries[index]
            time_sum += duration if time_itv >= duration else time_itv
        return time_sum + duration
