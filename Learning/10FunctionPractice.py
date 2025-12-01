# Nth Fibonacci (Recursion)
def fib (n):
    if(n <= 1):
        return n
    return fib(n-1) + fib(n-2)
a = int(input("Enter n to find nth fibonacci: "))
fib(a)


# Check Palindrome
strb = input("Enter string to check palindrome or not: ")
def palindrome(s):
    i, j = 0, len(strb) - 1
    while i < j:
        if(strb[i] != strb[j]):
            return False
        i += 1
        j -= 1
    return True

# Return (sum of digits, reverse, product)
def digit(n):
    s = 0, r = 0, p = 1, temp = n
    while temp > 0:
        d = temp % 10
        s += d
        r = r * 10 + d
        p *= d
        temp //= 10
    return s, r, p

c = int(input("Enter number to find sum of digits, reverse, product"))
digit(c)

# Remove duplicates but keep order
def removeDuplicate(arr):
    seen = set()
    result = []
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

# Character with highest frequency
def maxFrequency(strd):
    freq = {}
    for ch in strd:
        freq[ch] = freq.get(ch, 0) + 1
    return max(freq, key = freq.get)
strd = input("Enter string to check highest frequency of character")

# Count vowels and consonants
def count(stre):
    vowels = "aeiouAEIOU"
    v = c = 0
    for ch in stre:
        if ch in vowels:
            v += 1
        else:
            c += 1
    return v, c

# Merge two sorted lists
def sorting(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

# Check anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Find maximum using args
def find_max(*nums):
    m = nums[0]
    for x in nums:
        if x > m:
            m = x
    return m
