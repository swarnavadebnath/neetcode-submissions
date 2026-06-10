class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        GP = dummy
        while True:
            kth = GP
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
            if not kth:
              break  
            # FIXED: Indented all of this to be INSIDE the while loop
            GN = kth.next
            prev = GN
            curr = GP.next
            while curr != GN:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = GP.next
            GP.next = kth
            GP = temp
        return dummy.next