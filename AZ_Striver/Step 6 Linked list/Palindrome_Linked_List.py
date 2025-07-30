def isPalindrome(head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
 
        t = head
        s =  []
        while t is not None:
            s.append(t.val)
            t=t.next
        t = head
        while t is not None:
            tt = s.pop()
            if t.val != tt:
                return False
            t = t.next

        return True
