# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        my_set= set()

        while current is not None:
            if current in my_set:
                return True
            my_set.add(current)
            current = current.next

        return False