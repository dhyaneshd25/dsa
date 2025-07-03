def ispalindromeString(n):
    first_index=0
    last_index=len(n)-1
    while first_index<last_index:
        if n[first_index]!=n[last_index]:
            return False
        first_index+=1
        last_index-=1
    return True

def ispalindromeInteger(n):
    #reverse the number
    if n<0:
        return False
    reverse_number = 0
    temp = n
    while temp>0:
        last_digit = temp%10
        reverse_number=reverse_number*10+last_digit
        temp = temp//10
    if reverse_number ==n:
        return True
    else:
        return False

print(ispalindromeString("aadaa"))
print(ispalindromeInteger(88))