# 7장 배열
import math
from typing import List


class Solution:
    # p.173
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, v in enumerate(nums):
            maps[v] = i
        for i, v in enumerate(nums):
            if target - v in maps and i != maps[target - v]:
                return [i, maps[target - v]]

    # p.180
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2 or max(height) == 0:
            return 0

        volume = 0
        lbar_max, rbar_max = 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            lbar_max = max(lbar_max, height[left])
            rbar_max = max(rbar_max, height[right])

            if lbar_max <= rbar_max:
                volume += lbar_max - height[left]
                left += 1
            else:
                volume += rbar_max - height[right]
                right -= 1
        return volume

    # p.184
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [nums]

        nums.sort()
        for k in range(len(nums) - 3):
            left, right = k + 1, len(nums) - 1
            while left < right:
                sum_nums = nums[k] + nums[left] + nums[right]
                if sum_nums == 0:
                    if [nums[k], nums[left], nums[right]] not in result:
                        result.append([nums[k], nums[left], nums[right]])
                    left += 1
                elif sum_nums < 0:
                    left += 1
                else:
                    right -= 1
        return result

    # p.190
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    # p.193 -> memoization
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        result = []
        for l in range(len(nums)):
            result.append(prod)
            prod *= nums[l]
        prod = 1
        for r in range(len(nums) - 1, -1, -1):
            result[r] *= prod
            prod *= nums[r]
        return result

    # p.195 -> 체크하기
    def maxProfit(self, prices: List[int]) -> int:
        result, min_p = 0, prices[0]
        for k in range(1, len(prices)):
            if prices[k] <= min_p:
                min_p = prices[k]
            else:
                if result < prices[k] - min_p:
                    result = prices[k] - min_p
        return result
