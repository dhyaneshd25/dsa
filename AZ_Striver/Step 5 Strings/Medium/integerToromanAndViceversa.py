def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    value_symbols = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    t=num
    i=0
    ans = ""
    while t>0:
        d = t//value_symbols[i][0]
        if d>0:
            ans+=d*value_symbols[i][1]
        t=t%value_symbols[i][0]
        i+=1
    return ans






def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    ss=dict()
    ss['I']=1
    ss['V']=5
    ss['X']=10
    ss['L']=50
    ss['C']=100
    ss['D']=500
    ss['M']=1000
    ans = 0
    j=len(s)-1
    while j>=0:
        if j+1<len(s):
            if ss[s[j]]<ss[s[j+1]]:
                ans-=ss[s[j]]
            else:
                ans+= ss[s[j]]
        else:
                ans+= ss[s[j]]
        j-=1
    return ans
        
