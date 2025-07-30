def middleNode(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast =  head
        while fast is not None and fast.next is not None and slow.next is not None:
                slow = slow.next
                fast = fast.next.next
        return slow