#recursion
def rev(head,prev):
    if prev is None:
        return head
    temp = prev.next
    prev.next = head
    head = prev
    return rev(head,temp)
def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # #iterative
    # if head is None or  head.next is None:
    #     return head
    
    # first = head
    # second = head.next
    # thrid = head.next.next
    # first.next = None
    # second.next = first
    # while thrid is not None:
    #     temp = thrid
    #     thrid = thrid.next
    #     temp.next = second
    #     second = temp
    # return second
    # recurrsion
    node = None
    node = rev(node,head)

    return node