class Solution:
    def hasDuplicate(self, nums):
        ans = set()

        for j in range(len(nums)):
            if nums[j] in ans:
                return True
            ans.add(nums[j])

        return False