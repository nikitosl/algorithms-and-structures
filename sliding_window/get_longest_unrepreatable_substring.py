def get_char_index(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    return None


def get_longest_unrepreatable_substring(s: str) -> int:
    seen = {}
    index_l, index_r = 0, 0
    max_len = 0
    while index_r < len(s):
        char = s[index_r]
        if char in seen and seen[char] >= index_l:
            index_l = seen[char] + 1
        else:
            max_len = max(max_len, index_r - index_l + 1)
        seen[char] = index_r
        index_r += 1

    return max_len

example, result = "pwwkew", 3
print(get_longest_unrepreatable_substring(example))
print(get_longest_unrepreatable_substring(example) == result)
