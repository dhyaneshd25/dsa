first_number = 0
second_number = 1

n=int(input())

print(first_number,end=' ')
print(second_number,end=' ')

for i in range(n-2):
    third_number = first_number+second_number
    print(third_number,end=' ')
    first_number = second_number
    second_number = third_number