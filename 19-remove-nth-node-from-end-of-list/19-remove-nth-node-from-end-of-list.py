# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return
        
        # calculate desired pos
        length = self.linked_list_length(head)
        pos = length - n + 1
        
        if pos == 1:
            temp = head.next
            head.next = None
            return temp
        
        # # edge case
        # if pos < 0 or pos > length:
        #     return
        
        # traverse ll to pos
        curr_node = head
        prev_node = None
        curr_pos = 1
        
        while curr_node:
            if curr_pos == pos:
                prev_node.next = curr_node.next
                return head
            prev_node = curr_node
            curr_node = curr_node.next
            curr_pos += 1
            
    def linked_list_length(self, head): # [1,2]
        curr_node = head
        length = 0
        while curr_node:
            curr_node = curr_node.next
            length += 1
        return length
        