
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i in range(len(nums)):
            remain = target - nums[i]

            if remain in hash_map:
                return [hash_map[remain], i]
            else:
                hash_map[nums[i]] = i

        return []
