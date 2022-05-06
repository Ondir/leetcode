# Main list
lst_a = [24, 17, 16, 27, 59]

# ALL items are in lst_a
lst_b = [59, 37, 32, 40]


print(list(set(lst_a).intersection(set(lst_b))))

#
#
# for i in range(0, len(list2)):
#     l = 0
#     r = len(list1)-1
#     while l < r:
#         n = int((r + l) / 2)
#         if list2[i] > list1[n]:
#             l = n + 1
#         else:
#             r = n
#     if list2[i] == list1[l]:
#         print('YES')
#     else:
#         print('NO')
#
#


# nums = [1,3,11,11,15,13,11,14]
#
# fac = len(nums)-len(set(nums))
# print(fac)
# print( (sum(nums)-sum(list(set(nums)))))
#
#
# print(
#     int(sum(nums)- sum(list(set(nums))))/fac
# )
#



#
# last2, last1 = nums[0], nums[1]
# # print("last2 = ", nums[0], 'last1 = ', nums[1])
# # edge case: first and last are the same
# # print(nums[0], nums[-1])
# if nums[0] == nums[-1]:
#     print(nums[0])
#
# for i in range(2, len(nums)):
#     # print('i =',i)
#     # the number must be one of the 2 previous numbers, at some point
#     # print("last1 = ",last1, 'numns = ', nums[i])
#     # print("last2 = ", last2, 'numns = ', nums[i])
#     if last1 == nums[i] or last2 == nums[i]:
#         print(nums[i])
#     else:  # reset the previous 2 numbers
#         temp = last1
#         # print("temp = ", temp)
#         last1 = nums[i]
#         # print("last1 = ", nums[i])
#         last2 = temp
#         # print("last2 = ", last2)
#
#
#
# # print(len(nums))
# # print(set(nums))
# # print(len(set(nums)))
# #
# # fac = len(nums)-len(set(nums))
# # print('fac= ', fac)
# # print(sum(nums)-sum(list(set(nums))))
# # print( int((sum(nums)-sum(list(set(nums))))/fac))
#
# # for i in range(1, len(nums)):
# #     print(i, i - 1)
# #     print("nums[i]")
# #     print(nums[i], nums[i - 1])
# #     if nums[i] == nums[i - 1]:
# #         # found duplicate, return
# #        print(nums[i])
# # print("end for")
# #
# # print(nums[-2], nums[0])
# # if nums[-2] == nums[0]:
# #     # [X, a, X, b, ..., X, z], return nums[-2]
# #     print(nums[-2])
# # else:
# #     # [a, X, b, X, ..., z, X] or
# #     # [X, a, X, b, ..., z, X], return nums[-1]
# #     print(nums[-1])