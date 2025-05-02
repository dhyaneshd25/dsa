matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

#brute force O(N^2) and space O(N^2)
def rotate_approach1(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        dy = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        r=0
        c=len(matrix[0])-1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                   dy[r][c]=matrix[i][j]
                   r+=1
            c-=1
            r=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=dy[i][j]
                
rotate_approach1(matrix)
print(matrix)

#optimal O(N^2) and space O(1)
'''
first find the transpose of the matrix
then reverse the each row of the matrix
'''
def rotate_approach2(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):     
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            j=0
            k=len(matrix[i])-1
            while j<k:
                matrix[i][j],matrix[i][k]=matrix[i][k],matrix[i][j]
                j+=1
                k-=1
rotate_approach2(matrix)
print(matrix)