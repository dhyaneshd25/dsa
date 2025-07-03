matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def spiralOrder(matrix):
        ans=[]
        t=0
        l=0
        r=len(matrix[0])-1
        b = len(matrix)-1

        while t<=b and l<=r:
            for i in range(l,r+1):
                ans.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                ans.append(matrix[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    ans.append(matrix[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    ans.append(matrix[i][l])
                l+=1
        return ans
    
print(spiralOrder(matrix))