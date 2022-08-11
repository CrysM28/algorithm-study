# 3) bisect 사용 풀이

import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        
        if idx<len(nums) and nums[idx] == target:
            return idx
        else:
            return -1