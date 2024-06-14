def column_wise_addition(num1, num2, base):  #The function column_wise_addition is defined in this line, and it requires three parameters: base, num1, and num2.
    
    digits = "0123456789ABCDEF"  #The valid digits for integers in bases 2 to 16 are represented by a string of digits created by this line.
    result = "" #Creates a new, empty string result to hold the column-wise addition result.
    overflow = 0 #sets the carry or overflow when adding digits to a variable called overflow, and initializes it to 0.
    #line 7 and 8 make processing easier,we reverse the input integers,by num1 and num2. This enables the addition to begin with the rightmost, or least significant, digit. 
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    maximum_length = max(len(num1), len(num2)) #Determines the maximum length between num1 and num2. This is done to make sure that each digit in both numbers is covered by the loop.
    
    for i in range(maximum_length): #Initiates a loop that iterates through each digit, going from the least to the most important.
        
        if i<len(num1): #In order to prevent index out of range errors, determines whether i is inside num1's range.
            digit1 = digits.index(num1[i])
        else:
            digit1 = 0

        if i<len(num2): #Also this one in order to prevent index out of range errors, determines whether i is inside num2's range.
            digit2 = digits.index(num2[i]) 
        else:
            digit2 = 0
        column_sum = digit1+digit2+overflow #Determines the total of the overflow from the preceding column as well as the current digits in numbers 1 and 2.

        if column_sum>=base: #Verifies whether the total exceeds or equals the base to see if there is an overflow or carry.
            overflow = 1
            column_sum -= base
        else:
            overflow = 0
        result = digits[column_sum] + result #It adds the digit (character) that corresponds to column_sum to the result before it in the digits string.

    if overflow: #Checks to see if, after processing every digit, there is still an overflow.
        result = "1" + result #This appends a '1' to the outcome in the event of a final carry.
    return result #Returns the addition's final result when done column-wise

base = 16 #This sets the hexadecimal number's base to 16.
#line 39 and 40 establishes num1 and num2's values for the addition.
num1 = "2A"  
num2 = "3F"
result = column_wise_addition(num1, num2, base) #This uses num1, num2, and base as parameters when calling the column_wise_addition method, and it saves the outcome in result.
print("Outcome in base",base,":",result) #Prints the column-wise addition result in the given base. 
