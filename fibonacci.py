N= int(input("Enter the number \n"))

fib =[0, 1]

if N < 1:
    print("Invalid Input")
elif N==1 :
    print([0])
elif N==2 :
    print(fib)
else :

    for i in range( 2, N+1 ):
         nextnum = fib[i-1] + fib[i-2]
         fib.append(nextnum)

    print(fib)