# Importing the mySQL.connector module to python

import mysql.connector 

# Getting the details of connection from the user

host = input("Enter the name of host: ")
user = input("Enter the name of user: ")
passwd = input("Enter the password: ")

# Connecting python to mySQL through the information given by user

mydb = mysql.connector.connect(host = host, user = user , passwd = passwd)
mycur = mydb.cursor()

# Display the database available in the server

database = 'show databases'
mycur.execute(database)
print('The list of databases are: ')
for X in mycur:
    print(X)

# Getting the database 

db = input("Enter your database: ")
dbs = 'use {}'.format(db)
mycur.execute(dbs)

# Displaying the tables available in the database 

s = 'show tables'
mycur.execute(s)
print('The list of tables in {} are: '.format(db))

for Y in mycur:
    print(Y)
tab = input("Enter the table name: ")

# Implementing a function for a menu driven program

def customize():
    while True:
        print('Menu!!!')
        print("\n 1.Add (To add columns in the selected table) \n 2.Modify (To change the datatype of the selected table) \n 3.Drop columns (To drop any column from the selected table) \n 4.Show (To display values from the selected table) \n 5.Insert (To insert values in the selected table) \n 6.Custom (Acts as a terminal) \n 7.Arrange \n 8.End (To break)")
        x = int(input("Enter your choice: "))

        if x == 1:
            y = input("Enter column name to be added in {} table: ".format(tab))
            z = input("Enter the datatype: ")
            p = 'alter table {} add {} {}'.format(tab,y,z)
            mycur.execute(p)
            print("Column '{}' has been sucessfully added to table {}".format(y,tab))
            dis = input("Do you want to display the table(Y for yes): ")

            if dis.lower() == 'y':
                show = 'show columns from {}'.format(tab)
                mycur.execute(show)
                for X in mycur:
                    print(X[0],end =' ')
                disp = 'select * from {}'.format(tab)
                mycur.execute(disp)
                for Y in mycur:
                    print(Y)
            
            else:
                continue
            mydb.commit()
            
        elif x == 2:
            y = input("Enter name of the column to be modified in {} table: ".format(tab))
            z = input("Enter the datatype of column {}: ".format(y))
            p = 'alter table {} modify {} {}'.format(tab,y,z)
            mycur.execute(p)
            print("column '{}' of table '{}' has been changed to '{}' datatype".format(y,tab,z))
            dis = input("Do you want to display the table(Y for yes): ")

            if dis.lower() == 'y':
                show = 'show columns from {}'.format(tab)
                mycur.execute(show)
                for X in mycur:
                    print(X[0],end =' ')
                disp = 'select * from {}'.format(tab)
                mycur.execute(disp)
                for Y in mycur:
                    print(Y)

            else:
                continue
            mydb.commit()

        elif x == 3:
            y = input("Enter name of the column to be dropped from {} table: ".format(tab))
            p = 'alter table {} drop {}'.format(tab,y)
            mycur.execute(p)
            print("The column '{}' from table '{}' have been removed".format(y,tab))
            dis = input("Do you want to display the table(Y for yes): ")

            if dis.lower() == 'y':
                show = 'show columns from {}'.format(tab)
                mycur.execute(show)
                for X in mycur:
                    print(X[0],end =' ')
                disp = 'select * from {}'.format(tab)
                mycur.execute(disp)
                for Y in mycur:
                    print(Y)
                    
            else:
                continue
            mydb.commit()   

        elif x == 4:
            y = input("Enter the column to display in {} table(* for all the columns): ".format(tab))
            z = input("Enter the condition: ")
            if z == '':
                p = 'select {} from {}'.format(y,tab,z)
            else:
                p = 'select {} from {} where {}'.format(y,tab,z)
            mycur.execute(p)
            for X in mycur:
                print(X)
            mydb.commit()
            
        elif x == 5:
            y = input("Enter the names of columns where values are added in {} table(seperated by Commas): ".format(tab))
            z = input("Enter the values of corresponding columns in {} table: ".format(tab))
            p = 'insert into {}({}) values({})'.format(tab,y,z)
            mycur.execute(p)
            print("Value inserted successfully")
            dis = input("Do you want to display the table(Y for yes): ")

            if dis.lower() == 'y':
                show = 'show columns from {}'.format(tab)
                mycur.execute(show)
                for X in mycur:
                    print(X[0],end =' ')
                disp = 'select * from {}'.format(tab)
                mycur.execute(disp)
                for Y in mycur:
                    print(Y)

            else:
                continue
            mydb.commit()
            
        elif x == 6:
            y = input('Enter your custom command: ')
            p = '{};'.format(y)
            mycur.execute(p)
            for X in mycur:
                print(X)
            dis = input("Do you want to display the table(Y for yes): ")

            if dis.lower() == 'y':
                show = 'show columns from {}'.format(tab)
                mycur.execute(show)
                for X in mycur:
                    print(X[0],end =' ')
                disp = 'select * from {}'.format(tab)
                mycur.execute(disp)
                for Y in mycur:
                    print(Y)

            else:
                continue
            mydb.commit()
        
        elif x == 7:
            y = input("Enter any column name to be displayed: ")
            p = input("Enter any condition: ")
            q = input("Enter a column to be arranged: ")
            z = input("Enter asc or desc: ")
            if p == "":
                if z == "asc":
                    mycur.execute("select {} from {} order by {}".format(y,tab,q))
                    for i in mycur:
                        print(i)
                elif z == "desc":
                    mycur.execute("select {} from {} order by {} desc".format(y,tab,q))
                    for j in mycur:
                        print(j)
            elif p != "":
                if z == "asc":
                    mycur.execute("select {} from {} where {} order by {}".format(y,tab,p,q))
                    for k in mycur:
                        print(k)
                elif z == "desc":
                    mycur.execute("select {} from {} where {} order by {} desc".format(y,tab,p,q))
                    for k in mycur:
                        print(k)

        elif x == 8:
            print("Thank you for using this program")
            break

customize()
        


