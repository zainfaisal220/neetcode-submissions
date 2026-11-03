from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        return sorted(hash_map, key=hash_map.get, reverse=True)[:k]