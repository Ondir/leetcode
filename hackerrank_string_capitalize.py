def solve(s):

    return ' '.join([i.capitalize() for i in s.split(' ')])

s = 'chris alan'

numb = 'hello   world  lol'

g = solve(numb)
print(g)
