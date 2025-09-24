'''Reema mirghani 433006218'''

"""This program is to find which catagory a triangle belongs in given 3 inputs"""
def triangle_type_checker(a,b,c):
    ''' the function uses if elif to determine triangle type'''
    if a==b and b==c and a==c:
        return ("equalatral trigangle")
    elif a==b or b==c or a==c:
        return ("isoclesles triangle")
    elif a!=b and a!=c and b!=c:
        return("scalene triangle")
    
def main():
    a=int(input("enter first side of triangle"))
    b=int(input("enter second side of triagnel"))
    c=int(input("enter third side of triangle"))
    print("your triangle is an",triangle_type_checker(a,b,c))
main()
          



              
            
