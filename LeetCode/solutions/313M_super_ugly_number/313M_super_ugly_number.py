# 313. Super Ugly Number
# 
# Write a program to find the nth super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the given 
# prime list primes of size k.
# 
# Example:
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
#              super ugly numbers given primes = [2,7,13,19] of size 4.
# Note:
# 
#   - 1 is a super ugly number for any given primes.
#   - The given numbers in primes are in ascending order.
#   - 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
#   - The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        index = [0] * len(primes)
        n -= 1
        while n > 0:
            nextUglies = []
            for i in range(len(primes)):
                nextUglies.append(ugly[index[i]] * primes[i])

            uglyMin = min(nextUglies)
            ugly.append(uglyMin)

            for i in range(len(primes)):
                if uglyMin == ugly[index[i]] * primes[i]:
                    index[i] += 1

            n -= 1

        return ugly[-1]

def test():
    print('Testing nthSuperUglyNumber(self, n, primes)...\n')

    s = Solution()

    n = 12
    primes = [2, 7, 13, 19]
    result = s.nthSuperUglyNumber(n, primes)
    print('Expected:  32')
    print('Output:    ' + str(result) + '\n')

test()