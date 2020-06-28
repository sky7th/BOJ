def solution(s):
    if len(s) == 1:
        return 1

    min_compressed_str_len = len(s)
    for size_to_compare in range(1, len(s) // 2 + 1):
        compressed_str = compress_str(s, size_to_compare)
        if len(compressed_str) < min_compressed_str_len:
            min_compressed_str_len = len(compressed_str)

    return min_compressed_str_len


def compress_str(s, size_to_compare):
    now = s[0:size_to_compare]
    compressed_str = ''
    count = 0
    for i in range(0, len(s) * 2, size_to_compare):
        target = s[i:i + size_to_compare]
        if now == target:
            count += 1
            continue

        if count == 1:
            compressed_str += now
        else:
            compressed_str += str(count) + now

        now = target
        count = 1

    return compressed_str


print(solution("abcabcdede"))