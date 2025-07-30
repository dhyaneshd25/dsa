def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    l = 0
    t= head
    while t is not None:
        l+=1
        t=t.next
    if l==n:
        return head.next
    i = 0
    t =  head
    while i<l-n-1:
        t= t.next
        i+=1
    t.next = t.next.next
    return head