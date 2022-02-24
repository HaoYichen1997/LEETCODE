'''
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import quicksort as qs
import binarysearch as bs
def twosum1(nums:list[int], target: int) -> list[int]: # brute force
    result = list()
    for i, num1 in enumerate(nums):
        for x, num2 in enumerate(nums[i+1:]):
            if num1 + num2 == target:
                result.append(i)
                result.append(i+x+1)
                print("first num in:", i, "\nsecond num in:", i + x + 1)
                break
        if result:
            break

    return result
"""
时间复杂度 O(n^2)  
这样写更好
 for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:

"""

def twosum2(nums:list[int], target: int) -> list[int]:
    qs.quicksort(nums, 0, len(nums)-1)
    for i in range(len(nums)-1):
        x = bs.binary_search(nums, 0, len(nums), target - nums[i])
        if x != -1 and x != i:
            return i, x
'''
快排和二分查找时间复杂度都是O(nlogn)， 因此算法也是O(nlogn)
'''

def twosum3(nums:list[int], target: int) -> list[int]:
    hashtable = dict()
    for i, j in enumerate(nums):
        if target - j in hashtable:
            return [hashtable[target - j], i]
        else:
            hashtable[nums[i]] = i


'''
python 中dict就是散列表（哈希表），查找哈希表中的元素耗时O（1）
因此算法时间复杂度为O(n)
'''
result = twosum2([3,3], 6)
print(result)