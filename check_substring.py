"""
Q: You are given two strings. Check if the first string is a subsequence of the other string. A subsequence of a string
   is when the new string is formed by deleting some or none elements of the original list. Important thing is that
   characters positions relative to each other must be preserved
"""

def isSubsequence(s, t):
    idx_s = 0
    idx_t = 0
    while True:
        if s[idx_s] == t[idx_t]:
            idx_s += 1
            idx_t += 1
        elif s[idx_s] != t[idx_t]:
            idx_t += 1
        if idx_t == len(t):
            break
    return idx_s == len(s)

flag = isSubsequence("abc","ahbgdc")
print("is substring:", flag)
flag = isSubsequence("axc","ahbgdc")
print("is substring:", flag)

