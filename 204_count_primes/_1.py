import unittest


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1] * n
        i = 2
        while i * i < n:
            if primes[i]:
                j = i * 2
                while j < n:
                    primes[j] = 0
                    j += i
            i += 1
        return sum(primes[2:n])


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(4, s.countPrimes(10))


if __name__ == '__main__':
    unittest.main()
