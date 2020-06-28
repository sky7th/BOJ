def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(0, len(s) - i + 1):
            if is_palindrome(s[j:j + i]):
                return len(s[j:j + i])
    return 1


def is_palindrome(s):
    half = len(s) // 2
    return s[:half] == s[::-1][:half]