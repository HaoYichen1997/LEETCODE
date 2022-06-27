'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
length / x = y ... n
第一和最后一行至少有y 其余至少有2y
若 n<= row 前n个有2y+1 第一行y+1 row - n 有2y 和y
n> row 下标为[2row - n-1:row-1] 实际加1
第一行的特点是原str中 为除 2 rows -2 余1 的位置 ，放到list中就是余数为0的下标
最后一行是除2rows -2 余 rows 的位置，下标为rows-1
其他行为余行数加余2rows- 2 -行数 的位置， 交替来。 因此余数下标为 i为行数
i - 1 和 2rows -3 -i

做了一年不想做了，下面是leetcode上的源码
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)



