def transform_number(num):
    number = num
    for sumb in ('(', ')', '+', '-'):
        number = number.replace(sumb, '')
    if len(number) == 11:
        number = number[1::]
    elif len(number) == 7:
        number = '495' + number
    return number


num_add = transform_number(input())
nums = []
for i in range(3):
    if transform_number(input()) == num_add:
        print("YES")
    else:
        print("NO")
