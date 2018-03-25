# -*- coding:utf-8 -*-
import math

class Solution():
    def solve(self, A):
        # call function prime
        result = []
        for i in A:
            if self.prime(i):
                result.append(i)
        return result


    # judge whether x is prime or not
    def prime(self, x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
             if x % i == 0:
                 return False
        return True
