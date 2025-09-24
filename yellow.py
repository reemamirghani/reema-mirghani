# def equal(SIDES):
#     return SIDES*3
# def main():
#     yoyo=equal(5)
#     print(yoyo)
# main()

# total=0
# number=100
# while  number>=0:
#     total=total+number
#     number=number-2
# print(total)

# def find_sum():
#     total=0
#     number=1
#     while number>=0:
#         total=number+total
#         number=number-1
#         print(total)

number=int(input("enter a number"))
total=0
while True:
    if number==0:
        break
    elif number%5==0:
        number=int(input("enter a number"))
        continue
    else:
        total=total+number
        number=int(input("enter a number"))
print(total)
    