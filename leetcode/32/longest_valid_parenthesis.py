"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Example 3:

Input: ")((())"
Output: 4
Explanation: The longest valid parenthesis sybstring is "(())"

example:
    stack = (
    stack = ((
    stack = (()
        -> stack = 2(
    iter through stack, add up consecutive numbers
"""


class Solution:
    def longest_valid_parenthesis(self, s):
        stack = [-1]
        length = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if stack:
                    length = max(length, i - stack[len(stack) - 1])
                else:
                    stack.append(i)

        return length


class Test:

    def test_longest_valid_parenthesis(self):
        solution = Solution()
        assert solution.longest_valid_parenthesis("(()") == 2
        assert solution.longest_valid_parenthesis(")((())") == 4
        assert solution.longest_valid_parenthesis(")()())") == 4
        assert solution.longest_valid_parenthesis("()(())") == 6
        assert solution.longest_valid_parenthesis("())()()") == 4
        assert solution.longest_valid_parenthesis("()(()") == 2 # need to account for this -- returns 4
