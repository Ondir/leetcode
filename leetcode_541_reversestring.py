s = "abcdefg"
k = 2
ans = ''
for i in range(0, len(s), 2*k):
    print(s[i:i+k][::-1]+s[i+k:i+2*k])
    ans +=s[i:i+k][::-1]+s[i+k:i+2*k]
