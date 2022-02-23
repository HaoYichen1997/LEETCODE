'''
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import Twosum as twosum
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        b = list()
        length =len(nums)
        for i in range(length):
            a = list()
            a = twosum.twosum3(nums[i+1:],-nums[i])
            a.insert(0,i)
            b.append(a)
        return b

sol=Solution()
result = sol.threeSum([-1,0,1,2,-1,-4])
print(result)