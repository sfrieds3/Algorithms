'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0, 1, 2, 4, 5, 6, 7] might become[4, 5, 6, 7, 0, 1, 2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Example 2:

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
'''


class Solution:
    def search(self, nums, target: int) -> int:
        '''
        known: target, len(list)
        start at nums[target]:
            if num > target:
            if num < target:
        '''

        result: int = -1

        list_mid: int = len(nums) // 2
        test_val: int = nums[list_mid]
        list_length: int = len(nums)


        if test_val == target:
            result = list_mid
        else:
            try:
                dist_to_target = list_length - (test_val - target)
                if nums[list_mid + 1 + dist_to_target] == target:
                    result = list_mid + 1 + dist_to_target
            except:
                result = -1

            if result == -1:
                dist_to_target = (target - test_val)
                print("expected: " + str(target))
                print(dist_to_target)
                try:
                    print(nums[list_mid + dist_to_target])
                    if nums[list_mid + dist_to_target] == target:
                        result = list_mid + dist_to_target
                except:
                    result = -1
        return result


class Test:
    def testSearch():
        solution: Solution = Solution()
        solution_list = [4, 5, 6, 7, 0, 1, 2]
        assert(solution.search(solution_list, 0) == 4)
        assert(solution.search(solution_list, 3) == -1)
        assert(solution.search(solution_list, 7) == 3)
        assert(solution.search(solution_list, 5) == 1)


if __name__ == "__main__":
    Test.testSearch()
