# Time:  O(1)
# Space: O(w)

from collections import deque
import sys


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.__size = size
        self.__sum = 0
        self.__q = deque([])

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += val
        self.__q.append(val)
        return 1.0 * self.__sum / len(self.__q)

obj = MovingAverage(12)

while True:
        out=[]
        out.append([])
        out.append([])
        read = float(sys.stdin.readline())
        out[0] = read
        value = obj.next(read)
        out[1]= value
        print out



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)