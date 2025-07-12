def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        ans = 0
        res = ""
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         if (j-i+1)>ans and s[i:j+1]==s[i:j+1][::-1]:
        #                 res = s[i:j+1]
        #                 ans = j-i+1
        for i in range(len(s)):
            d = s[i]
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>len(res):
                    res=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>len(res):
                    res=s[l:r+1]
                l-=1
                r+=1
        return res