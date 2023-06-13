# WAP to display the multiplication table of a given number

def multable(x,y):
    for i in range(1,y+1):
        print("{} x {} = {}".format(x,i,x*i))

a = int(input("Enter a number to be multiplied: "))
b = int(input("Enter the total number: "))
multable(a,b) 
