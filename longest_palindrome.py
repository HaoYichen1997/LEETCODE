'''
给你一个字符串 s，找到 s 中最长的回文子串。
'''
import copy
class Solution:
    '''
    暴力解 O(n^3)
    '''
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
    动态规划 DYNAMIC PROGRAMMING
    '''
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        longest_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n+1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > longest_len:
                            longest_len = j - i + 1
                            begin = i
        return s[begin:begin + longest_len]


sol = Solution()
result = sol.longestPalindrome1("babad")
print(result)