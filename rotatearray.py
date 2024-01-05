class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<k:
            k=k%n
        li1 = list(reversed(nums[n - k:]))
        li2 = list(reversed(nums[:n - k]))
        main = li2 + li1
        main.reverse()
        for i in range(n):
            nums[i] = main[i]
