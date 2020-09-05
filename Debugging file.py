class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums = sorted(nums, key=lambda x: str(x) * 10, reverse=True)
        return ''.join(nums) if nums[0] != '0' else '0'


sol = Solution()
print(sol.largestNumber([5, 67, 7, 83, 9, 0]))

print(list(map(lambda x: str(x) * 2, [5, 67, 7, 83, 9, 0])))

print(len(max(['5', '67', '7', '83', '9', '0'])))


# bubble sort
class Solution:
    def largestNumber(self, nums) -> str:
        n = len(nums)
        for idx in range(n):
            nums[idx] = str(nums[idx])
        for idx in range(n - 1):
            for jdx in range(idx + 1, n):
                a, b = nums[idx], nums[jdx]
                if int(a + b) < int(b + a):
                    nums[idx], nums[jdx] = nums[jdx], nums[idx]

        if nums and nums[0] == '0':
            return '0'
        return "".join(nums)




#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1>x2 and v1>=v2) or (x2>x1 and v2>=v1):
        print('NO')
    else :
        if (abs(x1-x2)%abs(v1-v2) )==0:
            print("Yes")
        else:
            print("no")
        # k1 = x1
        # k2 = x2
        # while k1<=10000 and k2<=10000:
        #     if k1 == k2 :
        #         print("YES")
        #         break
        #     else:
        #         k1 = k1+v1
        #         k2 = k2+v2
        # print("NO")


x1 = 1113

v1 = 612

x2 = 1331

v2 = 610

result = kangaroo(x1, v1, x2, v2)



