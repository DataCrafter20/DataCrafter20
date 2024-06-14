def is_non_decreasing(num):
    num_str = str(num)
    return all(num_str[i] <= num_str[i+1]for i in range(len(num_str)-1)) 

def non_decreasing_square(x):
    for n in range(1, x):
        if is_non_decreasing(n) and is_non_decreasing(n**2):
            print(n ,"and" , n**2)
x = 40
non_decreasing_square(x)