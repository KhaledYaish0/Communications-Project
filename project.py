
import random

def calc_redundant_bits(m): #This function calculates the number of redundant bits
    for i in range(m):      #needed for error detection and correction based on the length of the data.
        if(2**i >= m + i + 1):#m is the length of data and i is the number of redundant bits.
            return i

def position_redundant_bits(data, r):#This function inserts redundant bits (initialized to 0) into the data at positions that are powers of 2.
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

def calc_parity_bits(arr, r):         #This function calculates the parity for each redundant bit and updates the redundant bits in the data.
    n = len(arr)                                 #arr is the binary string with redundant bits placed, and r is the number of redundant bits.
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detect_error(arr, nr):                                       #This function detects if there is any error in the received data.
    n = len(arr)                                                #arr is the received data, and nr is the number of redundant bits.
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
if not all(char in '01' for char in data):                # Check if all characters are binary
    print("Invalid input. Please enter a binary string.")
else:
    m = len(data)                                         #This line calculates the length of the input data and stores it in the variable m.
    r = calc_redundant_bits(m)                             #call for the function

    arr = position_redundant_bits(data, r)                 #call for the function
    arr = calc_parity_bits(arr, r)                         #call for the function

    print("Data transferred is: " + arr)

    bit_to_invert = random.randint(0, len(arr) - 1)            #This line selects a random position in the data string to introduce an error.
    arr_with_error = arr[:bit_to_invert] + str(1-int(arr[bit_to_invert])) + arr[bit_to_invert+1:]#This line creates a new string 0->1/1->0
    print("Data with error introduced: " + arr_with_error)

    correction = detect_error(arr_with_error, r)
    print("The position of the error is: " + str(correction)) if correction else print("There is no error in the received data.")
    #Error Detection and Reporting: If the error is detected, the program prints the position of the error.
