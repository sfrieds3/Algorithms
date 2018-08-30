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
"""


class Solution:
    def longest_valid_parenthesis(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        algorithm:
        1) iterate until first "("
        2) if next == "(" add to left parens list, else add to right parens list
        3) iterate through remaining
        4)

        Input: ")((())"
        Output: 4
        Explanation: The longest valid parenthesis sybstring is "(())"

        left: [1,2,3,]
        right: [0,4,5]

        beg: 2
        end: 5
        answer: (5 - 2 + 1) = 4

        iterate through, add all "(" to stack

        stack = (

        """

        stack = []
        temp = 0
        length = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif stack:
                if stack.pop() == "(":
                    temp += 2
                else:
                    length = max(temp, length)
                    temp = 0
            else:
                length = max(temp, length)
                temp = 0

        length = max(length, temp)

        return length


class Test:

    def test_longest_valid_parenthesis(self):
        solution = Solution()
        assert solution.longest_valid_parenthesis("(()") == 2
        assert solution.longest_valid_parenthesis(")((())") == 4
        assert solution.longest_valid_parenthesis(")()())") == 4
        assert solution.longest_valid_parenthesis("()(())") == 6
        assert solution.longest_valid_parenthesis("())()()") == 4
        assert solution.longest_valid_parenthesis("()(()") == 2
