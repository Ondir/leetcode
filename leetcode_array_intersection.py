nums1 = [4, 9, 5]
nums2 = [2,2]

ans = []

for i in nums1:
    if i in nums2:
       ans.append(i)
       nums2.remove(i)

print(ans)