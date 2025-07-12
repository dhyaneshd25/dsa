def beauty(ss):
    m = dict()
    for sss in ss:
        if sss not in m:
            m[sss]=1
        else:
            m[sss]+=1
    mx = max(m.values())
    mn = min(m.values())
    return mx-mn
def beautySum(s):
    """
    :type s: str
    :rtype: int
    """


    ans=0
    for i in range(len(s)):
        for j in range(i,len(s)):
            ans+=beauty(s[i:j+1])
    return ans