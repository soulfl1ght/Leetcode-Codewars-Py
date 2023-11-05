class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        return x_str == x_str[::-1]
x=121
solution = Solution()
result = solution.isPalindrome(x)
print(result)