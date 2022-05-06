test_str = "BANANA"
vowel = ['A', 'E', 'I', 'O', 'U']
count = 0

for i in range(len(test_str)):
    for j in range(i+1, len(test_str)+1):
        if test_str[i] not in vowel:
            count+=1
print(count)
#
# res = [test_str[i: j] for i in range(len(test_str))
#           for j in range(i + 1, len(test_str) + 1) if test_str[0] not in vowel]
# print(res)