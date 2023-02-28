# Check Permutation

from collections import defaultdict

def isPermutation(s1, s2):
    if len(s1) != len(s2): return False

    hash = defaultdict(int)

    for char in s1:
        hash[char] += 1
        
    for char in s2:
        if hash[char] == 0: return False
        hash[char] -= 1

    return True

# O(n) where n is the length of the string

# Similar problem:
# https://leetcode.com/problems/valid-anagram/description/