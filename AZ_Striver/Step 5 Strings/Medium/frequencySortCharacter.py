def frequencySort(s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        newd = sorted(d.items(),key=lambda it :it[1],reverse =True)
        print(newd)
        ans = ""
        for i in newd:
           for j in range(i[1]):
              ans+=i[0]
        return ans