class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                if nums[i] + nums[j] == target:
                    arr.append(i)
                    arr.append(j)
                    return arr
                j += 1
            i += 1