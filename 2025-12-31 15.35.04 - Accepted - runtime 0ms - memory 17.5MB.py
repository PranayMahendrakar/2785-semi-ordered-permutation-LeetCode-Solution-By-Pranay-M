class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pos1 = nums.index(1)
        posn = nums.index(n)
        # Moves to bring 1 to front + moves to bring n to back
        # If 1 is after n, we save 1 swap
        swaps = pos1 + (n - 1 - posn)
        if pos1 > posn:
            swaps -= 1
        return swaps