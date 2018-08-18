# Problem:
# Given a string, find the length of the longest substring without repeating characters
# e.g. "abcabcbb" => "abc" with length of 3
#      "bbbbb" => "b" with length of 1
#      "pwwkew" => "wke" with length of 3


def find_longest_substring(s: str):
    longest_substring_length: int = 0
    current_substring_length: int = 0
    longest_substring: str = ""
    current_substring: str = ""

    for i in s:
        if (i in current_substring):
            while (i in current_substring):
                current_substring = current_substring[1:]
                current_substring_length = current_substring_length - 1
        current_substring = current_substring + i
        current_substring_length = current_substring_length + 1
        if (current_substring_length > longest_substring_length):
            longest_substring_length = current_substring_length
            longest_substring = current_substring

    if (longest_substring == ""):
        longest_substring = current_substring
        longest_substring_length = current_substring_length

    print("substring: " + longest_substring)
    print(longest_substring_length)

    return longest_substring


def test_find_longest_substring():

    assert find_longest_substring("test") == "tes"
    assert find_longest_substring("aab") == "ab"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("pwwkew") == "wke"
    assert find_longest_substring("aababbbsadfkadsfkjkgggggggabcdefghijklmnopqrst") == "abcdefghijklmnopqrst"
