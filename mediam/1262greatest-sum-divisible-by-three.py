lass Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)

        r1 = [x for x in nums if x % 3 == 1]
        r2 = [x for x in nums if x % 3 == 2]

        if total % 3 == 0:
            return total

        if total % 3 == 1:
            a = r1[0] if len(r1) >= 1 else float('inf')
            b = r2[0] + r2[1] if len(r2) >= 2 else float('inf')
            return total - min(a, b)

        if total % 3 == 2:
            a = r2[0] if len(r2) >= 1 else float('inf')
            b = r1[0] + r1[1] if len(r1) >= 2 else float('inf')
            return total - min(a, b)

       
