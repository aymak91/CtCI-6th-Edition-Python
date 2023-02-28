# Is Unique

def isUnique(s):
    visited = set()

    for letter in s:
        if letter in visited: return False
        visited.add(letter)
    return True

# O(n) where n is the length of the string

# If we were not allowed to use additional data structures, we would have to compare every combination of letters. O(n^2)
# If we were allowed to mutate the input, we can actually sort it and compare neighbors. O(nlogn)