# Letian Xu
# 01/15/2019
# I have not given or received any unauthorized assistance on this assignment.

# a. 
def check_prime(num):
    '''
    Argument: integer number
    Return: If the input integer is a prime number, return True;
            If the input integer is not prime number or not a valid input, return False.
    '''
    if isinstance(num, int) == False:
        return False
    # First I will check if it is an invalid input, like a decimal;
    # if it is, we will return false.
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
            # So, in the range(2, input itself), We test it by division;
            # whenever we have a remainder of 0, we will return false.
        else: 
            return True
            # On the contrary, if no remainder is 0, we return True.
    else: 
        return False
        # This is for we got 1 as the input.

# b.
def check_happy(num):
    '''
    Happy number definition:
    Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number either equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or sad numbers).

    Argument: integer number
    Return: If the input integer is a happy number, return True;
            If the input integer is not happy number or not a valid input, return False.
    '''
    if isinstance(num, int) == False or num < 0:
        return False
    # Check if it is a valid input    
    happy = set()
    # Using the set() constructor to store the number in a integar.
    while num not in happy:
        # Once the divided number appeared twice, it cannont be a happy number;
        # as long as the divided number doesn't appear again, it can keep process.
        happy.add(num)
        # Put the new sum result into set() constructor.
        num = sum([int(x) ** 2 for x in str(num)])
        # str() function transfer the integar into string; 
        # and the variable x refers to the scope of the generator passed to the any() function
        if num == 1:
            return True
    return False

# c. 
def check_happy_prime(num):
    '''
    Argument: integer number
    Return: If the input integer is a both happy and primenumber, return True;
            If the input integer is not both happy and prime number or not a valid input, return False.
    '''
    # If a integar get true from two functions above, it is a happy prime
    if check_prime(num) and check_happy(num) == True:
        return True
    else:
        return False

# d. 
def first_x_prime(num):
    '''
    Argument: integer number
    Return: a list with first input number of prime number.
    '''
    result = []
    count = 0 # The number of right number to count
    a = 2 # The number to test 
    while count <= num:
        if check_prime(a) == True:
            result.append(a)
            count +=1
        a +=1
    print('The first',num,'prime number are: ',result)

first_x_prime(20)

# e.
def first_x_happy(num):
    '''
    Argument: integer number
    Return: a list with first input number of happy number.
    '''
    result = []
    count = 0
    a = 2
    while count <= num:
        if check_happy(a) == True:
            result.append(a)
            count +=1
        a +=1
    print('The first',num,'happy number are: ',result)

first_x_happy(20)

# f. 
def first_x_happyprime(num):
    '''
    Argument: integer number
    Return: a list with first input number of both happy and prime number.
    '''
    result = []
    count = 0
    a = 2
    while count <= num:
        if check_happy_prime(a) == True:
            result.append(a)
            count +=1
        a +=1
    print('The first',num,'happy prime number are: ',result)

first_x_happyprime(20)

# g. 
def first_x_sadprime(num):
    '''
    Argument: integer number
    Return: a list with first input number of both prime and sad number.
    '''
    result = []
    count = 0
    a = 2
    while count <= num:
        if check_prime(a) == True and check_happy(a) == False:
            result.append(a)
            count +=1
        a +=1
    print('The first',num,'sad prime number are: ',result)

first_x_sadprime(20)
