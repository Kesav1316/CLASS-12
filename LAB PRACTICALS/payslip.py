while True:
   ide = int(input("Enter employees id: "))
   name = input("Enter employees name: ")
   grade = input("Enter employees grade: ")

   if grade == "A":
      basicpay = 5000
      HRA = 8/100*basicpay
      DA = 5/100*basicpay
      TA = 10/100*basicpay
      PF = 12/100*basicpay
      grosspay = HRA + DA + TA + basicpay
      netpay = grosspay - PF
      allowance = HRA + DA + TA
      deduction = PF
      print("\n Employee id : ",ide,"\n Employee name : ",name,"\n Grade: ",grade,"\n Basicpay: ",basicpay,"\n Allowance: ",allowance,"\n Deduction: ",deduction,"\n Grosspay: ",grosspay,"\n Netpay: ",netpay)
      x = input("Do you want to continue(Y for yes and N for no): ")
      if x == "Y":
         pass
      elif x == "N":
         print("Thank you for using our program")
         break
   elif grade == "B":
      basicpay = 7500
      HRA = 10/100*basicpay
      DA = 7/100*basicpay
      TA = 12/100*basicpay
      PF = 13/100*basicpay
      grosspay = HRA + DA + TA + basicpay
      netpay = grosspay - PF
      allowance = HRA + DA + TA
      deduction = PF
      print("\n Employee id : ",ide,"\n Employee name : ",name,"\n Grade: ",grade,"\n Basicpay: ",basicpay,"\n Allowance: ",allowance,"\n Deduction: ",deduction,"\n Grosspay: ",grosspay,"\n Netpay: ",netpay)
      x = input("Do you want to continue(Y for yes and N for no): ")
      if x == "Y":
         pass
      elif x == "N":
         print("Thank you for using our program")
         break
   elif grade == "C":
      basicpay = 10000
      HRA = 12/100*basicpay
      DA = 10/100*basicpay
      TA = 15/100*basicpay
      PF = 15/100*basicpay
      grosspay = HRA + DA + TA + basicpay
      netpay = grosspay - PF
      allowance = HRA + DA + TA
      deduction = PF
      print("\n Employee id : ",ide,"\n Employee name : ",name,"\n Grade: ",grade,"\n Basicpay: ",basicpay,"\n Allowance: ",allowance,"\n Deduction: ",deduction,"\n Grosspay: ",grosspay,"\n Netpay: ",netpay)
      x = input("Do you want to continue(Y for yes and N for no): ")
      if x == "Y":
         pass
      elif x == "N":
         print("Thank you for using our program")
         break
