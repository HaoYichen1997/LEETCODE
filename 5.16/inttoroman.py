'''
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给你一个整数，将其转为罗马数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-roman
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        number = num; roman = list()
        roman.append(["M"]*(number // M))
        number = number - M * (number // M)
        if number // 100 < 5:
            if number // 100 == 4:
                roman.append(["CD"])
            else:
                roman.append(["C"] * (number // C))
        else:
            if number // 100 == 9:
                roman.append(["CM"])
            else:
                roman.append(["D"])
                number = number - 500
                roman.append(["C"] * (number // C))
        number = number - C * (number // C)

        if number // 10 < 5:
            if number // 10 == 4:
                roman.append(["XL"])
            else:
                roman.append(["X"] * (number // X))
        else:
            if number // 10 == 9:
                roman.append(["XC"])
            else:
                roman.append(["L"])
                number = number - 50
                roman.append(["X"] * (number // X))
        number = number - X * (number // X)

        if number < 5:
            if number == 4:
                roman.append(["IV"])
            else:
                roman.append(["I"] * number)
        else:
            if number == 9:
                roman.append(["IX"])
            else:
                roman.append(["V"])
                number = number - 5
                roman.append(["I"] * number)
        roman1 = ''
        for i in roman:
            roman1 = roman1 + ''.join(i)
        return roman1

sol = Solution()
result = sol.intToRoman(3876)
print(result)
'''
时间复杂度O(1)
'''
'''
答案方法1： 把4,9这些也算进来，不停地减。 应该注意到按最大的数值从上往下减就可以了。
思路

根据罗马数字的唯一表示法，为了表示一个给定的整数 num，我们寻找不超过 }num 的最大符号值，将num 减去该符号值，
然后继续寻找不超过num 的最大符号值，将该符号拼接在上一个找到的符号之后，循环直至num 为 00。最后得到的字符串即为num 的罗马数字表示。

编程时，可以建立一个数值-符号对的列表 valueSymbols，按数值从大到小排列。遍历 valueSymbols 中的每个数值-符号对，
若当前数值 value 不超过 num，则从 num 中不断减去 value，直至 num 小于 value，然后遍历下一个数值-符号对。若遍历中 num 为 00 则跳出循环。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcod-75rs/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
VALUE_SYMBOLS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def intToRoman1(self, num: int) -> str:
    roman = list()
    for value, symbol in Solution.VALUE_SYMBOLS:
        while num >= value:
            num -= value
            roman.append(symbol)
        if num == 0:
            break
    return "".join(roman)
'''
法2， 按每一位转换成已经枚举的特定字符串。 不搬过来了。
'''