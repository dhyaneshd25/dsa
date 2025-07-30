def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    # t = headA
    # while t is not None:
    #     tt = headB
    #     while tt is not None:
    #         if t == tt:
    #             return tt
    #         tt =  tt.next
    #     t = t.next
    # return None
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a