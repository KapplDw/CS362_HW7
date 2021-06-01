## Dwight Kappl

# print 1- 100
# Fizz on multiples of 3
# Buzz on multiples of 5
# FizzBuzz on multiples of 3 and 5


def fizzbuzz(x):
    if(x % 3) == 0 and (x % 5) == 0:
        return "FizzBuzz"
    elif(x % 3) == 0:
        return "Fizz"
    elif(x % 5) == 0:
        return "Buzz"
    else:
        return x


for i in range(0, 101):
    print(fizzbuzz(i))
