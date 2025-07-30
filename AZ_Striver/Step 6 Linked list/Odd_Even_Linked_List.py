def oddEvenList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head is None or head.next is None:
        return head
    odd = None
    to  =  odd
    even = None
    te = even
    t  =  head
    ck =  True
    while t is not None:
        tt = t
        t=t.next
        if ck:
            if to is None:
                odd = tt
                to = tt
            else:
                to.next = tt
                to = tt
            ck = False
        else:
            if te is None:
                even = tt
                te = tt
            else:
                te.next = tt
                te = tt
            ck = True

    te.next = None
    to.next = even
    return odd