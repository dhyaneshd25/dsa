def findcommonprefix(p,q):
    l = min(len(p),len(q))
    i = 0
    ans = ""
    while i<l:
        if p[i]!=q[i]:
            break
        ans+=p[i]
        i+=1
    return ans
def longestCommonPrefix( strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 1:
        return strs[0]
    ans = findcommonprefix(strs[0],strs[1])
    for i in range(2,len(strs)):
        p  = findcommonprefix(strs[i],strs[i-1])
        if len(ans)>len(p):
            ans= p
    return ans