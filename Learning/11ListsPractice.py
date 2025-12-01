# Given a list of numbers, return a new list containing only prime numbers.
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def findPrime(arr):
    return [n for n in arr if prime(n)]

# Rotate list right by k (no slicing)
def rotate(arr, k):
    k %= len(arr)
    for _ in range(k):
        last = arr.pop()
        arr.insert(0, last)
    return arr

# Longest increasing array
def longestIncreasingArray(arr):
    maxLen = 1, currLen = 1, start = 0, newStart = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            currLen += 1
        else:
            if currLen > maxLen:
                maxLen = currLen
                newStart = start
            start = i
            currLen = i
    if currLen > maxLen:
        maxLen = currLen
        newStart = start
    
    return arr[newStart: newStart + maxLen]

# Keep only elements with highest frequency
from collections import Counter
def highFreq(arr):
    freq = Counter(arr)
    highest = max(freq.values())
    return [n for n in arr if freq[x] == highest]

# Second largest element unique number
def secondLargest(arr):
    unique = list(set(arr))
    unique.sort(reverse=True)
    return unique[1] if len(unique) >= 2 else None

# Rearrange lists
def rearrange(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    return evens + odds
