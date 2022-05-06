def isPalindrome(x: int) -> bool:
    y = [ int(str(x)[i]) for i in range(len(str(x))-1, -1, -1)]
    x1 = int(''.join(list(map(str, y))))
    print(x1)
    print(x==x1)

x = 121

print(isPalindrome(x))



