
nums = [47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]
n = None
slow = fast = head
while fast:
    t1, t2 = slow.next, fast.next.next
    slow.next = n
    n = slow
    slow, fast = t1, t2

ans = -1
while n:
    ans = max(ans, n.val + slow.val)
    n, slow = n.next, slow.next
return ans