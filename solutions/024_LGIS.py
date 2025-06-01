# Find longest increasing subsequence (LIS) and longest decreasing subsequence

def subsequence(p: list) -> list[int]:
    l = [1] * len(p)
    for i in range(len(p)):        # Finds the length of LIS
        for j in range(i+1, len(p)):
            if p[i] < p[j]:
                l[j] = max(l[j], l[i] + 1)
    # l now holds the length of LIS at each index
    lis = []
    max_len = max(l)    # LIS length
    # Iterates backwards so that only the elements of LIS are added
    for i in range(len(p) - 1, -1, -1):
        if max_len == l[i]:
            lis.append(p[i])
            max_len -= 1
    return lis[::-1]        # lis is backwards, so lis[::-1] reverses it
