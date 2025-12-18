# Checking if the two strings are Anagram or not
s1 = 'listen'
s2 = 'silent'
s1 = sorted(s1.lower())
s2 = sorted(s2.lower())
if s1 == s2:
    print("Anagram")
else:
    print("Not anagram")
