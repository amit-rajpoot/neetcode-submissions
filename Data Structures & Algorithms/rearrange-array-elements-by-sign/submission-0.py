class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0]*n
        pos_idx = 0
        neg_idx = 1

        for i in range(0,n):
            if nums[i] > 0:
                result[pos_idx] = nums[i]
                pos_idx += 2
            else:
                result[neg_idx] = nums[i]
                neg_idx += 2
        
        return result
        