import numpy as np
import random

def calc_redundant_bits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def position_redundant_bits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]

def calc_parity_bits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detect_error(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val*(10**i)
    return int(str(res), 2)

# Get user input for data
data = input("Enter the data (binary string): ")

# Validate user input
if not all(char in '01' for char in data):
    print("Invalid input. Please enter a binary string.")
else:
    m = len(data)
    r = calc_redundant_bits(m)

    arr = position_redundant_bits(data, r)
    arr = calc_parity_bits(arr, r)

    print("Data transferred is: " + arr)

    bit_to_invert = random.randint(0, len(arr) - 1)
    arr_with_error = arr[:bit_to_invert] + str(1-int(arr[bit_to_invert])) + arr[bit_to_invert+1:]
    print("Data with error introduced: " + arr_with_error)

    correction = detect_error(arr_with_error, r)
    print("The position of the error is: " + str(correction)) if correction else print("There is no error in the received data.")
