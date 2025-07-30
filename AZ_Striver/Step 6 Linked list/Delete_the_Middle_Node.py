def deleteMiddle(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if head is None or head.next is None:
        return None
    if head.next.next is None:
        head.next =  None
        return head

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    if slow.next is None:
        slow = None
    else:
        slow.val = slow.next.val
        slow.next = slow.next.next
    return head