class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteMiddle(head, n):
    if n == 1:
        return None

    mid = n // 2
    prev = None
    curr = head

    for _ in range(mid):
        prev = curr
        curr = curr.next

    prev.next = curr.next
    return head

n = int(input().strip())
vals = list(map(int, input().split()))

head = Node(vals[0])
temp = head
for v in vals[1:]:
    temp.next = Node(v)
    temp = temp.next

head = deleteMiddle(head, n)

temp = head
while temp:
    print(temp.val, end=" ")
    temp = temp.next
