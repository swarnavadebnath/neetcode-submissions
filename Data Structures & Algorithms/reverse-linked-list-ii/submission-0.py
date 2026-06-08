# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        for _ in range(left-1):
            pointer = pointer.next
        cur = pointer.next
        prev = None
        for _ in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        pointer.next.next = cur
        pointer.next = prev
        return dummy.next
        
            



        