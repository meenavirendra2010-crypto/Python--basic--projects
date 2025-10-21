# first mini project
print("Your Welcome")
a=int(input("please enter number a:"))
b=int(input("please enter number b:"))    
print("please enter n for your desire operation")
print("enter 1 for + ")
print("enter 2 for - ")
print("enter 3 for * ")
print("enter 4 for / ")
print("enter 5 for % ")

n=int(input("enter n:"))
if n==1:
      print("result:",a+b)
elif n==2:
      print("result:",a-b)
elif n==3:
      print("result:",a*b)
elif n==4:
        if b==0:
            print("division is not defined by zero.")
        else:
            print("result",a/b)
elif n==5:
      print("result:",a%b)

print("PLEASE REVISIT!")
print("THANK YOU")
