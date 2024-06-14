def convert_base(number,from_the_base,to_the_base):# A function named convert_base which changes a number's base from one to another.

    return format(int(number,from_the_base),'0'+str(to_the_base)+'b') #function with binary representation ('b'), the input number is converted from from_the_base to to_the_base.


first_number = "11" #Assigns the variable first_number the value of the string "11".
first_base = 8 #Assigns the variable first_base with the integer value of 8.
second_number = "24" #Assigns the variable second_number the value of the string "24".
second_base = 5 #The variable second_base is assigned the integer 5.
result_base = 2 #The variable result_base is set to the integer 2.
result = convert_base(second_number,second_base,result_base) #Calls the convert_base function with second_number, second_base, and result_base as parameters and stores the output in result.

print(f"Result: {result} (base{result_base})") #Prints the result along with its base in a formatted string.


