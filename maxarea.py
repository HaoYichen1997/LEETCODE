'''
给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。

找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maxArea(self, height: list) -> int:
        length = len(height)
        max_area = 0
        for i in range(length):
            for j in range(i+1, length):
                if (j - i) * min(height[j], height[i]) > max_area:
                    max_area = (j - i) * min(height[j], height[i])
        return max_area
    '''
    暴力解 超时了 O(n^2)
    '''
    def maxArea1(self, height: list) -> int:
        l, r = 0
        max_area = 0
        length = len(height)
        r = length - 1
        while r > l:
            area = (r - l) * min(height[r], height[l])
            if area > max_area:
                max_area = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area
    '''
    答案的双指针解法， 经典题。
    指针一开始指向数组边界，把边界比较小的数向内缩1，视为新的边界。
    数学证明这种方式可以取得最大容积
    此时又是指向边界的双指针，用同样的解法。
    时间复杂度O(n)
    '''