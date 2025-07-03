def isIsomorphic( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    lens = 0
    lent  = 0
    dicts = dict()
    dictt  = dict()

    for i in range(len(s)):
        if s[i] not in dicts:
            dicts[s[i]]=i
            lens +=1

        if t[i] not in dictt:
            dictt[t[i]]=i
            lent +=1
        
        if dictt[t[i]] != dicts[s[i]]:
            return False
    return True