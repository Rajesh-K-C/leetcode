class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            need = target - nums[i]
            for j in range(i+1, len(nums)):
                if(need == nums[j]):
                    return [i,j]
        return None
