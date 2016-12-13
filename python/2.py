# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # new is a time-consuming process
        Add = 0
        answerhead = ListNode(0)
        answer = answerhead
        while l1 and l2:
            sumbit = l1.val + l2.val + Add
            answer.val = sumbit % 10
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                answer.next = ListNode(0)
                answer = answer.next
            if sumbit >= 10:
                Add = 1
            else:
                Add = 0

        if not (l1 or l2):
            if Add:
                answer.next = ListNode(1)
            return answerhead
        else:
            l = l1 if l1 else l2
            answer.next = ListNode(0)
            answer = answer.next
        while l:
            if not Add:
                answer.val = l.val
                answer.next = l.next
                return answerhead
            sumbit = l.val + Add
            answer.val = sumbit % 10
            if l.next:
                answer.next = ListNode(0)
                answer = answer.next
            if sumbit >= 10:
                Add = 1
            else:
                Add = 0
            l = l.next
        if Add:
            answer.next = ListNode(1)
        return answerhead
                
