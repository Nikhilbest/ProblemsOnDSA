class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)>1:
            nums.sort()
            for i in range(len(nums)):
                if nums[i]==nums[i-1]:
                    return True
            return False
