def convert_to_title(A):
    result = ""
    while A > 0:
        remainder = (A - 1) % 26
        result = chr(65 + remainder) + result
        A = (A - 1) // 26

    return result

input1 = 1
output1 = convert_to_title(input1)
print(output1)

input2 = 28
output2 = convert_to_title(input2)
print(output2)
