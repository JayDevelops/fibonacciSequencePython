def fibonacciSequence(until):
    fibArray = [0, 1]
    if until < 0:
        print("Incorrect value, please write a number bigger than one")
    elif until <= len(fibArray):
        return fibArray[until - 1]
    else:
        tempFib = fibonacciSequence(until - 1) + fibonacciSequence(until - 1)
        fibArray.append(tempFib)
        return tempFib

# Have the user enter an integer

userInteger = int(input("Please input a number it will add the Fibonacci Sequence until this value:"))
print(fibonacciSequence(userInteger))
