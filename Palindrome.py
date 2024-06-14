def is_palindrome(sentence): # a function named is_palindrome that accepts a parameter called sentence.
    sentence = ''.join(char for char in sentence if char.isalnum()).lower()#Converts the sentence to lowercase and eliminates characters that are not alphanumeric by using ''.join() and char.isalnum() functions.
    return sentence==sentence[::-1] #Determines whether a sentence is a palindrome by checking if it remains the same when reversed.

text = input("Enter a sentence:") #Receives input from the user for a sentence.
if is_palindrome(text): #Calls the is_palindrome function to determine if the provided text is a palindrome
    print("A Palindrome sentence") #Outputs "A Palindrome sentence" when the input is a palindrome.
else: #If the input is not palindrome
    print("Not a palindrome sentence") #Outputs "Sentence is not a palindrome"