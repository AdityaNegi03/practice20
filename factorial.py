def factorial(N):
    ans = 1

    for i in range(1, N + 1):
        ans = ans * i

    return ans


N = int(input("Enter the number to find the factorial : "))

print("Factorial of " + str(N) + "= " + str(factorial(N)))
