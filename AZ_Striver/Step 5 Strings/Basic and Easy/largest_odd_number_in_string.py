def largestOddNumber( num):
    """
    :type num: str
    :rtype: str
    """
    # ans = ""
    # temp = 0
    # curr = 0
    # for i in range(len(num)):
    #     if int(num[i])%2!=0:
    #         temp = max(temp,int(num[i]))
    #     curr = curr*10 + int(num[i])
    #     if curr%2!=0:
    #         temp = max(temp,curr)
    # if temp == 0:
    #     return ""
    # return str(temp)
    i = len(num)-1
    while i>=0:
        if int(num[i])%2!=0:
            break
        i-=1
    return num[:i+1]
    