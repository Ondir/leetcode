"""
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
Read More
For beginners like me, here are some more explanations.
"When acting on an array element A[index], the rest of the values of A remain the same."

When we add things from query to A[index], the rest of A is not changed. Thus, we do not need to
calculate the sum of the whole array A every time after we perform the addition.
This saves lots of time, since we are not traversing the whole array A for query.length times.
Instead, we only traverse the array A only once.
"Let's remove A[index] from S if it is even, then add A[index] + val back (if it is even.)"

If we don't perform Sum(A) every time after addition, what do we do?
We find the sum of the even numbers in A first. We will perform modifications on this "sum"
instead of traverse A to find a new sum every time after addition.
Now let's look at the elements at A that is going to change.
if A[index] is an even number, we remove it from sum. Why?
We already added it to our "sum". If after the addition, this number becomes odd, we won't want it anymore.
if A[index] is an odd number, we don't touch it. We didn't add it to our "sum".
Then we check the result after the addition.
if A[index]+val is even:
we add the whole "A[index]+val" to our sum, since it's even.
recall that , we subtracted A[index] in our previous step. we want to add everything back.
if A[index]+val is odd:
we don't do anything.
since it's odd, we don't want it in our sum.
we already subtracted A[index] from sum if it was even.
we didn't add A[index] to our sum if it was odd.
therefore, we don't need any extra steps here.
Now look again at the examples. I hope this helped.
The principle is, try to not recalculate the whole thing again and again. Avoid wasting resources at all costs.
Another way can be, and might be easier to understand, but takes extra steps:
we check the A[index]+val first. then check A[index]
"""


nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

total_sum_even = (sum (x for x in nums if x%2 == 0))
print(total_sum_even)
total_arr = []

for value, index in queries:
    if nums[index]%2 == 0:
        total_sum_even-=nums[index]
    nums[index]+=value
    if nums[index]%2 == 0:
        total_sum_even+=nums[index]
    total_arr.append(total_sum_even)

print(total_arr)













# curr_even_sum = sum(x for x in nums if x %2 ==0)
# output =[]
#
# for value, index in queries:
#     print("index = ", index, "value = ", value)
#     if nums[index] % 2 == 0:
#         curr_even_sum -= nums[index]
#         print(curr_even_sum)
#     nums[index] += value
#     print("nums = ", nums)
#     if nums[index] % 2 == 0:
#         curr_even_sum += nums[index]
#     print("final curr_even_sum", curr_even_sum)
#
#     output.append(curr_even_sum)
#     print("final output = ", output)
# print(output)
#
# print(curr_even_sum)
# total_all = []
# que = []
# for k, v in enumerate(queries):
#     nums[v[1]] = nums[v[1]]+v[0]
#     total_all.append(sum(filter(lambda x: (x%2 == 0), nums)))
# print(total_all)




# que = []
# total_all = []
#
# for k, v in enumerate(nums):
#
#     que.append(queries[k][0]+v)
# for k, v in enumerate(nums):
#     print("k = ", k, "v = ", v)
#
#     nums[k] = que[k]
#     print("temp[k] after = ", nums)
#     total_all.append(sum(filter(lambda x: (x%2 == 0), nums)))
#     # print(total_all)
#     # temp.clear()
