class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if nums [i] + nums[k] == target:
                    return [i,k]
                
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)

        