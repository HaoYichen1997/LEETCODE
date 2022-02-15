'''
给你一个字符串 s，找到 s 中最长的回文子串。
'''
import copy
class Solution:
    def longestPalindrome(self, s: str) -> str:
        wordlist = list(s)
        length = len(wordlist)
        longest_palindrome = list()
        palindrome = list()
        length_pal = 0
        for i, word in enumerate(wordlist):
            for j in range(i + 1,length):
                if wordlist[j] == word:
                    a = i; b = j; c = True
                    while a < b:
                        if wordlist[a] != wordlist[b]:
                            c = False
                            break
                        else:
                            a += 1; b -= 1
                    if c:
                        palindrome.clear()
                        for n in range(i, j + 1):
                            palindrome.append(wordlist[n])
                        length_pal = len(palindrome)
                        if length_pal > len(longest_palindrome):
                            longest_palindrome = copy.deepcopy(palindrome)
        if length == 1:
            return wordlist[0]
        if len(longest_palindrome) == 0:
            return wordlist[0]
        str2 = ''.join(longest_palindrome)
        return str2
'''
暴力解 O(n^3)
'''
sol = Solution()
result = sol.longestPalindrome("babad")
print(result)