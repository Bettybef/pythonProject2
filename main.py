 # Calculator using python
#1. addition
# 2. Subtract
# 3. Multiply
# 4. Divide


print("1.Add")
print("2.Subtract")
print("3 Multiply")
print("4.Divide")

choice = input("enter your choice : ")
num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
if choice == "1":
     print( num1,"+" ,num2, "=", (num1+num2))
elif choice =="2":
     print (num1,"-", num2, "=",(num1-num2))
elif choice =="3":
     print (num1,"*", num2, "=", (num1*num2))
elif choice =="4":
     if num2 ==0.0:
         print("Divide by 0 error ")
     else :
        print (num1, "/" ,num2, "=", (num1/num2))


else:
    print("invalid choice")


