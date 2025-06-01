# Find longest increasing subsequence (LIS) and longest decreasing subsequence

def subsequence(p: list) -> list[int]:
    l = [1] * len(p)
    for i in range(len(p)):        # Finds the length of LIS
        for j in range(i+1, len(p)):
            if p[i] < p[j]:
                l[j] = max(l[j], l[i] + 1)
    # l now holds the length of LIS at each index
    ssq_arr = []
    max_len = max(l)    # LIS length
    for i in range(len(p) - 1, -1, -1):
        if max_len == l[i]:
            ssq_arr.append(p[i])
            max_len -= 1
    return ssq_arr[::-1]
