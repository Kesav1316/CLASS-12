x = eval(input("Enter a dictionary: "))
y = eval(input("Enter a key to be updated: "))
z = eval(input("Enter the value to be changed: "))
def update(a,b):
    x[a] = b
    print(x)
update(y,z)

