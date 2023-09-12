# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution 1: Using a Hashmap
class Solution:
    def hasCycle(self, head) -> bool:
        visited_node = set()
        while head:
            if head in visited_node:
                return True
            else:
                visited_node.add(head)
                head = head.next
        return False


# Solution 2: Using two pointers one fast and one slow pointer
class Solution:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
