print ("write the number you want to know even or odd and prime or not")
X = int(input())

if (X % 2) == 0:
    print("even")

else:
    print('odd')
  
#X=int(input())

if (X == 1):
    print( "is not a prime number")

if (X == 2) : 
    print("is a prime number")
       
elif (X > 1):   
   for i in range(2 , X):
        if ((X % i) == 0):
           print("is not a prime number")
           break
        else:
            print("is a prime number")      

else:
    print("is not a prime number")

for i in range (X+1):
    if (((i % 3) == 0) and ((i %  5) != 0)):
        print("codingo") 

    elif i % 5 == 0 and  X %  3 != 0:
        print("joe")
    
    elif i % 3 ==0 and  X % 5 ==0:
        print("yousef")
