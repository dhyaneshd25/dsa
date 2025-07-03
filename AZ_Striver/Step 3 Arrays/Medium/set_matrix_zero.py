matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]


#brute force O(n^3) and space O(n^2)   [O((N*M)*(N+M)) and O(N*M)]
def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        vis = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # we could not use vis = [[0]*len(matrix[0])]*len(matrix)  it creates multiple references to the same list.
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0 and  vis[i][j]==0:
                    for k in range(0,len(matrix[i])):
                        if matrix[i][k]!=0:
                            matrix[i][k]=0
                            vis[i][k]=1
                    for k in range(0,len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j]=0
                            vis[k][j]=1
setZeroes(matrix)
print(matrix)


matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]


#optimal O(N^2) and space O(N) [O(2*N*M) and O(N+M)]
def setZeroes_approach2(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = [0 for _ in range(len(matrix))]
        c = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    r[i]=1
                    c[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if r[i]==1 or c[j]==1:
                    matrix[i][j]=0
setZeroes_approach2(matrix)
print(matrix)

matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
#optimal O(N^2) and space O(1) [O(2*N*M+N+M) and O(1)]
def setZeroes_approach3(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        c=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j==0:
                        c=0
                    else:
                         matrix[0][j]=0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(len(matrix[0])):
                    matrix[0][j]=0
        if c==0:                
            for j in range(len(matrix)):
                    matrix[j][0]=0

setZeroes_approach3(matrix)
print(matrix)