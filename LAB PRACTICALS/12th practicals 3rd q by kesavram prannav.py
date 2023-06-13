#WAP to pass list to a function and double the odd values and half the even values of the list and display the list after changing

x = eval(input("Enter a list with numbers: "))

def listchange(a):
    for i in range(0,len(x)):
        if x[i]%2==0:
            x[i]=x[i]/2
        else:
            x[i] = 2*x[i]
    print("Changed list is {}".format(x))

listchange(x)
