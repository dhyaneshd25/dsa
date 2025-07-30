from . import ListNode


def merge(left,right):
    ans = ListNode(-1,None)
    t=ans
    t1 = left
    t2 = right
    while t1 is not None and t2 is not None:
        if t1.val>t2.val:
            tt = t2
            t2=t2.next
            t.next = tt
            t =tt
            
        else:
            tt = t1
            t1= t1.next
            t.next = tt
            t =tt

    while t1 is not None:
        tt = t1
        t1= t1.next
        t.next = tt
        t =tt
    
    while t2 is not None:
        tt = t2
        t2=t2.next
        t.next = tt
        t =tt


    return ans.next


def sortList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # t = head
    # while t:
    #     tt = t.next
    #     while tt :
    #         if t.val>tt.val:
    #             t.val , tt.val = tt.val , t.val
    #         tt =  tt.next
    #     t=t.next
    # return head  
    if head is None or  head.next is None:
    # if not  head or not head.next:
        return head

    slow = head
    fast = head
    temp = None

    while fast is not None and fast.next is not None:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    temp.next = None
    left =  sortList(head)
    right = sortList(slow)
    return merge(left,right)