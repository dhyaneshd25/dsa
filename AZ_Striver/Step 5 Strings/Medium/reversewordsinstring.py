def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    ans = ""
    list_char = list(map(str,s.split(" ")))
    i=0
    while i<len(list_char):
        if list_char[i]=="":
            list_char.pop(i)
        else:
            i+=1

    for i in range(len(list_char)-1,-1,-1):

        if list_char[i]!="":
            ans+=list_char[i]
        if i!=0:
            ans +=' '
    return ans
        