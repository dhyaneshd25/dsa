def removeOuterParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    count = 0
    ans = ""
    for i in range(0,len(s)):
        if s[i]=='(':
            count +=1
            if count>1:
                ans = ans + s[i]
        else:
            count -=1
            if count>0:
                    ans = ans + s[i]
    return ans