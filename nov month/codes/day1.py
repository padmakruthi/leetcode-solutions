#453. Minimum Moves to Equal Array Elements
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        return sum(num - min_val for num in nums)
