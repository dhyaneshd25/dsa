def maxDepth(s):
    """
    :type s: str
    :rtype: int
    """
    mx = 0
    c  = 0
    for i in range(len(s)):
        if s[i] == '(':
            c+=1
        elif s[i]==')':
            c-=1
        mx=max(mx,c)
    return mx