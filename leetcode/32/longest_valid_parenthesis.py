"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_of_left_parens = 0
        longest_valid_parenthesis = 0
        current_length = 0

        """
        algorithm:

        """


class Test:

    def test_longest_valid_parenthesis(self):
        solution = Solution()
        assert solution.longestValidParentheses("(()") == 2
