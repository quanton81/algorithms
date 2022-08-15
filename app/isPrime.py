num = 9523615597210453
arrayOfPrimes = [2]

def isPrimeSimple(num):
    flag = False

    if num > 1:
        numIntPart = int(num ** 0.5) + 1
        for i in range(3, numIntPart, 2):
            if (num % i) == 0:
                flag = True
                break

    return not flag

def isPrime(num):
    flag = False

    if num > 1:
        numIntPart = int(num ** 0.5) + 1
        for i in range(2, numIntPart):
            if (num % i) == 0:
                flag = True
                break

    return not flag

isPrimeNumberSimple = isPrimeSimple(num)

if isPrimeNumberSimple:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

isPrimeNumberSimple = isPrime(num)

if isPrimeNumberSimple:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")