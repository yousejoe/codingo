X=int(input("Enter a number: "))
if X == 1:
    print( "is not a prime number")

if X==2 : 
        print("is a prime number")
       
elif X > 1:
   
   for i in range(2,X):
       
    
       if (X% i) == 0:
           print(X,"is not a prime number")
           break
   else:
       print(X,"is a prime number")
       
else:
   print(X,"is not a prime number")