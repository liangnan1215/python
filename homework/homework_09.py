#-*- coding:utf-8 -*-

class Solution():
    def solve(self, A):
        result={}
        for i in range(0,10):
            result.setdefault(i,0)
        for i in A:
            for x in i:
                result[ord(x)-ord('0')]+=1
        return result
        pass