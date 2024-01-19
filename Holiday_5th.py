def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    reversed_x = 0
    while x != 0:
        pop = x % 10
        x //= 10

        # Check for overflow before updating the result
        if reversed_x > (INT_MAX - pop) // 10:
            return 0

        reversed_x = reversed_x * 10 + pop

    return sign * reversed_x
input1 = 123
output1 = reverse_integer(input1)
print(output1)

input2 = -123
output2 = reverse_integer(input2)
print(output2)
