def even_odd(x):
    '''jghrjkeghjkr'''
    
    if x%2==0:
        print("even")
    else:
        print("odd")
def square_number(x):
    square=x*x
    print(square)
def postive_negative(x):
    if x>0:
        print("postive")
    elif x<0:
        print("negative")
def square_number(x):
    square=x*x
    print(square)
def cube_number(x):
    cube=x*x*x
    print(cube)
def main():
    x=int(input("add a number"))
    print(even_odd(x))
    print(cube_number(x))
    print(square_number(x))
    print(postive_negative(x))

main()