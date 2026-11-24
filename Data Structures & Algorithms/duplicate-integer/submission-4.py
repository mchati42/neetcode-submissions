class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_1 = len(nums)
        len_2 = len(set(nums))
        if len_2 != len_1:
            return True
        else:
            return False

        