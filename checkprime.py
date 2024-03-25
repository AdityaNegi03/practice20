import math
def checkprime(N):
    flag = False
    if N <= 1 :
        return False
    else :

        for i in range(2,int(math.sqrt(N)+1)):
            if N % i == 0 :
                return False

    return True

N= int(input("Enter a number to be checked \n"))

if checkprime(N) == True:
    print("Number is Prime")
else :
    print("Not Prime")
