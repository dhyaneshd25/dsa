from . import ListNode

def addTwoNumbers(l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ans = 0
        t1 = l1
        t2 = l2
        ll1=0
        ll2=0
        while t1 and t2:
            ll1+=1
            ll2+=1
            s = ans + t1.val + t2.val
            r = s%10
            q = s//10
            ans =  q
            t1.val =  r
            t2.val = r
            t1 = t1.next
            t2 = t2.next

        while t1:
            ll1+=1
            q = (ans+t1.val)%10
            r = (ans+t1.val)//10
            t1.val =  q
            ans = r
            t1=t1.next
        while t2:
            ll2+=1
            q = (ans+t2.val)%10
            r = (ans+t2.val)//10
            t2.val =  q
            ans = r
            t2 = t2.next
        if ll1>ll2:
            if ans>0:
                temp = l1
                while temp.next:
                    temp = temp.next
                n = ListNode(ans)
                temp.next = n
            return l1
        if ans>0:
            temp = l2
            while temp.next:
                temp = temp.next
            n = ListNode(ans)
            temp.next = n
        return l2