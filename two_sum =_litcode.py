import datetime

now = datetime.datetime.now()
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        for num in nums:
            if i < len(nums) - 1:
                summ = num + nums[i + 1]
                if target == summ:
                    return [i, i + 1]
                i += 1

# test_case
lst1 = [2, 7, 11, 15]
trgt1 = 9
lst2 = [3, 2, 4]
trgt2 = 6

solution = Solution()
print(solution.twoSum(lst1, trgt1))
print(solution.twoSum(lst2, trgt2))

print('Time to execute: {}'.format(datetime.datetime.now() - now))


