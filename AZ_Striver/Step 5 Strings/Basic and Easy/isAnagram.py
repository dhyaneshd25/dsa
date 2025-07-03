def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = dict()
        dt = dict()

        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]]=1
            else:
                ds[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in dt:
                dt[t[i]]=1
            else:
                dt[t[i]]+=1
        return ds==dt