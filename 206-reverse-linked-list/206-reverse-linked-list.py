# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # 1<-2<-3->4->5
        prev_node = None
        curr_node = head
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            
            prev_node = curr_node
            curr_node = next_node
            
        return prev_node
        