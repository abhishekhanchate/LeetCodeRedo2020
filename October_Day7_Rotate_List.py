# Day 7
# Rotate List

# Given a linked list, rotate the list to the right by k places, where k is non-negative.

#Example 1:
#Input: 1->2->3->4->5->NULL, k = 2
#Output: 4->5->1->2->3->NULL
#Explanation:
#rotate 1 steps to the right: 5->1->2->3->4->NULL
#rotate 2 steps to the right: 4->5->1->2->3->NULL


#Example 2:
#Input: 0->1->2->NULL, k = 4
#Output: 2->0->1->NULL
#Explanation:
#rotate 1 steps to the right: 2->0->1->NULL
#rotate 2 steps to the right: 1->2->0->NULL
#rotate 3 steps to the right: 0->1->2->NULL
#rotate 4 steps to the right: 2->0->1->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        def get_length_tail(head):
            n = 1
            pt = head
            while pt.next:
                n+=1
                pt = pt.next
            return n, pt

        n, old_tail = get_length_tail(head)

        old_head = head

        k = k%n

        if not k:
            return head

        pt = head
        counter = n
        
        while pt.next:
            
            if counter - 1 == k:
                new_tail = pt
                new = pt.next
                break
            counter -= 1
            pt = pt.next
        
        
        new_tail.next = None
       
        old_tail.next = old_head

        return new