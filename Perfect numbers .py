def is_perfect_number(num):
    divisors = []
    for i in range(1,num):
        if num%i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    return False

def find_perfect_numbers(n):
    count = 0
    num = 1
    perfect_numbers = []
    while count<n:
        if is_perfect_number(num):
            perfect_numbers.append(num)
            count+= 1
        num+= 1
    return perfect_numbers

n = int(input("Enter the value of n: "))
perfect_numbers = find_perfect_numbers(n)
print(f"The first {n} perfect numbers are: {perfect_numbers}")
