s = "abcabcbb"

setchar = set()
l = 0
res = 0

for r in range(len(s)):
    print("s[r] = ", s[r])
    while s[r] in setchar:
        print('setchar = ', setchar)
        print('delete s[l] = ', s[l])
        setchar.remove(s[l])
        l+=1
        print('l= ',l)
    setchar.add(s[r])
    print('setchar after add', setchar)
    print("r - l + 1 = ",r - l + 1)
    res = max(res, r - l + 1)
    print(res)
print(res)


