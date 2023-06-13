# WAP to input n numbers to a tuple and pass it to a function and count number of even and odd numbers

x = eval(input("Enter a tuple: "))
def count(a):
    y = list(x)
    odd = 0
    even = 0
    for i in range(0,len(y)):
        if y[i]%2==0:
            even+=1
        else:
            odd+=1
    print("Number of even numbers in the tuple {} is {}".format(x,even))
    print("Number of odd numbers in the tuple {} is {}".format(x,odd))

count(x)
            
