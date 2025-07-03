def rotateString( s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        i = 0
        while i<len(s):
            new_goal = s[i:] + s[0:i]
            if goal==new_goal:
                return True
            i+=1
        return False
        # if len(s)!=len(goal):
        #     return False
        # return goal in (s+s)