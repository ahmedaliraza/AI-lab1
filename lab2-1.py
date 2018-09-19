



x=int(input("enter your first number"))


if x%4 == 0:
   if x%100 == 0:
     if x%400== 0:
           print("leap year",x)
     else:
         print("not leap year",x)
   else:
     print("a leap",x)
else:
  print("not leap year",x)
