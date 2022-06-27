'''
例如， 罗马数字 2 写做II，即为两个并列的 1 。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        if s == "":
            return 0
        mid = len(s) // 2
        if s in roman_dict:
            return roman_dict[s]
        sol = Solution()
        if s[:2] in roman_dict:
            a = roman_dict[s[:2]]
            s = s[2:]
            return a + sol.romanToInt(s)
        else:
            a = roman_dict[s[0]]
            s = s[1:]
            return a + sol.romanToInt(s)


roman_dict = {
"I"      :       1,
"V"      :      5,
"X"    :      10,
"L"      :      50,
"C"      :      100,
"D"     :      500,
"M"     :      1000,
"CM" : 900, "CD": 400, "XC" : 90, "XL": 40, "IX" : 9, "IV" : 4
}

sol = Solution()
result = sol.romanToInt("MCMXCIV")
print(result)

'''
时间复杂度 O(n) 题解思路用当小数在大数左侧时，如10在100左侧， 结果+10 变-10
'''