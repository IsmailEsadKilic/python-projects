def fibonacci(n):

    if n==0:
        return 0
    elif n == 1:
        return 1
    elif isinstance(n,int):
        return (fibonacci(n-1) + fibonacci (n-2))

print(fibonacci(int(input("sayı"))))

# 0 1 1 2 3 5 8 13