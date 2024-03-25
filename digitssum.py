def digitsum (N):
    ans=0
    while N > 0:
        ans=ans+ N%10
        N=N//10

    print("SUM of digits = " + str(ans))

N = int(input("Enter the number : \n"))

digitsum(N)