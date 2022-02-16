'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围[−2^31,2^31− 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路，看了题解。从后到前按位数把X的一位从前到后放到rev
对超出范围的数进行分类

'''
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        rev = 0
        while x != 0:
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            #负数时处理 digit
            if x < 0 and digit > 0:
                digit -= 10

            x = (x - digit) // 10
            rev = rev * 10 + digit

        return rev
