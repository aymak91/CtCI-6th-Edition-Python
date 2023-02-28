# Check Permutation

from collections import defaultdict

def isPermutation(s1, s2):
    if len(s1) != len(s2): return False

    hash = defaultdict(0)

    for char in s1:
        hash[char] += 1
        
    for char in s2:
        if hash[char] == 0: return False
        hash[char] -= 1

    return True
