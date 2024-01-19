# Given a number N, verify if N is prime or not.
# Return 1 if N is prime, else return 0.
# Example :
# Input : 7
# Output : True

def is_prime(N):
    if N <= 1:
        return False  # Not prime

    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False  # Not prime

    return True  # Prime

# Example usage:
input_number = 7
output = is_prime(input_number)
print("Output:", output)

