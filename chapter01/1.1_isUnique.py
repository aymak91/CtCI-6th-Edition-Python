# Is Unique

def isUnique(s):
    visited = set()

    for char in s:
        if char in visited: return False
        visited.add(char)
    return True

# O(n) where n is the length of the string

# If we were not allowed to use additional data structures, we would have to compare every combination of chars. O(n^2)
# If we were allowed to mutate the input, we can actually sort it and compare neighbors. O(nlogn)

def isUnique(s):
    s.sort()

    last_char = None

    for char in s:
        if char == last_char: return False
        last_char = char

    return True