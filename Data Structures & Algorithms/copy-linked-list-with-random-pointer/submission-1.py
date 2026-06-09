"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OTC = collections.defaultdict(lambda:Node(0))
        OTC[None]=None
        cur = head
        while cur:
            OTC[cur].val = cur.val
            OTC[cur].next = OTC[cur.next]
            OTC[cur].random = OTC[cur.random]
            cur = cur.next
        return OTC[head]