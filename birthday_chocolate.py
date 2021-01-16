from itertools import combinations

def birthday(s, d, m):
    count = 0
    s = [1, 2, 1, 3, 2]
    d=3
    m=2
    for i in range(len(s)):
        print(s[i:i+m])
        if sum(s[i:i+m]) == d:
            count += 1
    print(count)
birthday(s=[1, 2, 1, 3, 2], d=3, m=2)



A = [1, 4, 3, 2]
for i in A[::-1]:
    print(i, end=' ')