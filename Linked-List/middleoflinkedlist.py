#Approach 1: Using a different array
class Solution:
    def middleNode(self, head):
        nodes = []
        n = 0
        while head:
            nodes.append(head)
            n += 1
            head = head.next
        k = n // 2 if n % 2 else ceil(n/2)
        return nodes[k]

#Appraoch 2: Using two pointers
class Solution:
    def middleNode(self, head):
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow