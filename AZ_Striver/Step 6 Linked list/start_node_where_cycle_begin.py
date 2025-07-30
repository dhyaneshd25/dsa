def detectCycle( head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow =  head
        fast = head   
        ans = 0    
        ck = False
        while fast is not None and fast.next is not None and slow is not None:
            slow =  slow.next
            fast =  fast.next.next
            ans +=1
            if slow == fast:
                ck = True
                break
        if not ck:
            return None
        print(ans)
        while head!=slow:
            head = head.next
            slow = slow.next
        return head