#Nuseyba Mohammed
#501282985
#lab2


# --------------------------------------------------------------
# 1) TMU Letter Grade Converter
# --------------------------------------------------------------
def lettergrade(pct):
    
    '''
    A classic problem, but classics are classic for a reason.
    
    Assume that parameter 'pct' is an integer representing
    a percentage grade.
    
    Return the letter grade (as a string) corresponding to this 
    percentage. To keep things simple, we won't worry about +/-. 

    80 to 100 = A
    70 to 79  = B
    60 to 69  = C
    50 to 59  = D
    0  to 49  = F

    If the value of pct is outside this range, return None.

    '''
    if 80 <= pct <= 100:
        return "A"
    elif 70 <= pct <= 79:
        return "B"
    elif 60 <= pct <= 69:
        return "C"
    elif 50 <= pct <= 59:
        return "D"
    elif 0 <= pct <= 49:
        return "F"
    else:
        return None

# --------------------------------------------------------------
# 2) Duplicate Sequence Elements
# --------------------------------------------------------------
def duplicates(items):

    '''
    Assume that parameter 'items' is a sequence. Return a 
    string according to the following criteria:
    
    If items does not contain exactly three elements,
    return the string 'invalid input'
    
    if items contains three elements, and they're all the same,
    return the string 'three-of-a-kind'
    
    if items contains three elements, and two are the same,
    return the string 'two-of-a-kind'
    
    if items contains three elements, and none are the same,
    return the string 'one-of-a-kind'
        
    FOOD FOR THOUGHT:    
    This function should work on all three 
    sequence types we've seen - strings, lists, and tuples. 
    Do you have to do anything different for the different types, 
    or can your code be exactly the same regardless of the 
    sequence type? This is a VERY powerful notion in computer 
    science that you will explore further in future courses. 

    '''
    if len(items) != 3:
        return "invalid input"
    if len(items) == 3:
        i , j , k = items
        if i == j == k :
            return 'three-of-a-kind'
        elif i == j or i == k or k == j :
            return 'two-of-a-kind'
        elif i != j != k:
            return 'one-of-a-kind'

 
# --------------------------------------------------------------
# 3) Inversions of Three
# --------------------------------------------------------------
def inversions(items):

    '''
    Like the previous question, you may assume 'items' 
    is a sequence. Also like the previous question, it should
    not matter if items is a string, list, or tuple.
    
    If items does not contain exactly three elements,
    return the integer -1.
    
    If items contains exactly three values, return the number
    of inversions in the sequence.
    
    In a sequence, an 'inversion' is a pair of elements that 
    are out of order with respect to the sorted sequence.
    We will consider 'sorted' to mean ascending order.
    
    For example:
    
    The list [1, 2, 3] contains zero inversions, because 
    the list is in ascending order.
    
    The list [2, 1, 3] contains one inversion, because the
    2 and the 1 are out of order with respect to each other.
    
    The list [3, 2, 1] contains THREE inversions. The 3 is 
    out of order with respect to both 2 and 1 (two inversions)
    and the 2 is out of order with respect to 1 (one more inversion)
    for a total of three inversions. 
    
    For an added challenge, try solving this problem using as few
    comparisons (<, >, <=, >=) as possible.
    
    FOOD FOR THOUGHT:    
    Once you've solved this problem, think about how your code 
    would have to change if there were four elements, five elements, 
    six elements, etc. Notice how the complexity grows. 
    How many more comparisons would you need for four elements? 
    Five elements? 100 elements? 
    What is the relationship between the number of comparisons
    and the number of elements in the sequence? This is another 
    supremely important notion that we'll explore further towards
    the end of the course, and in future courses.
    
    '''
    if len(items) != 3:
        return -1
    
    count = 0
    
    
    if items[0] > items[1]:
        count += 1
    if items[0] > items[2]:
        count += 1
    if items[1] > items[2]:
        count += 1
    
    return count
       
    
    
# --------------------------------------------------------------
# 4) Increasing, Strictly or Otherwise?
# --------------------------------------------------------------   
def increasing(items, strict):   
    
    '''
    Once more, assume items is a sequence. The second parameter,
    'strict', is boolean (True or False)
    
    If items does not contain exactly three elements,
    return the string 'invalid input'
    
    If 'strict' is something other than True or False, 
    return the string 'invalid input'
    
    If the sequence contains three elements, we now want to
    determine if it is ascending. However, there's a twist - we
    will distinguish between ascending, and strictly ascending.
    
    If a sequence is ascending, every element is greater than 
    or equal to the one that came before it.
    
    If a sequence is strictly ascending, every element is 
    strictly greater than the one that came before it.
    
    If parameter 'strict' is True, you should test for
    strictly ascending. If it is False, check for simple
    ascending.
    
    In either case, return True if the 'items' is ascending,
    strict or otherwise, and False if not. 
    '''
    if len(items) != 3:
        return 'invalid input'
    if strict not in [True,False]:
        return 'invalid input'
    if strict:
        return items[0] < items[1] < items[2]
    else:
        return items[0] <= items[1] <= items[2]
   
   
# --------------------------------------------------------------
# 5) Python as a Calculator 
# --------------------------------------------------------------      
def calculator(op1, op2, operator):     
    
    '''
    This function accepts three arguments:
    op1, op2: assume both of these are integers
    operator: assume this argument is a string.
    
    This function should return the arithmetic result of the
    expression <op1> <operator> <op2>
    
    For example, if 'operator' is the string '+', return
    op1 + op2.
    
    Your function should recognize the following five operators:
    '+', '-', '*', '/', and '**'. 
    
    Additionally, your function should not perform division by
    zero. Implement the necessary check to ensure this doesn't 
    happen.
    
    If the operator is not one of the five above, or there
    would be a division by zero, return None.
    '''
    if operator == '+' :
        return op1 + op2
    elif operator == '-':
        return  op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '**':
        return op1 ** op2
    elif operator == '/':
        if op2 == 0:
            return None
        return op1 / op2
    else:
        return None    
    
    
    
    
    
# --------------------------------------------------------------
# 6) Summing Evens
# --------------------------------------------------------------
def sumeven(n):
    
    '''
    This function should calculate and return the sum of the 
    first n even numbers, where n >= 0. Note that 0 is even.
    
    For example, if n is 6, then the sum would be:

    0 + 2 + 4 + 6 + 8 + 10 = 30

    FOOD FOR THOUGHT:
    There are about a dozen different (yet equally 'good') ways 
    you could accomplish this. Once you've solved the problem,
    try solving it again using a different loop style, or a
    different way of producing the first n even integers. Or, 
    just maybe, you can come up with a way to solve this 
    without writing a loop at all?
    
    '''
    sum = 0
    for i in range(n):
        sum += 2 * i
    return sum


# --------------------------------------------------------------
# 7) Summing Squares
# --------------------------------------------------------------
def sumsquares(n):
    
    '''
    This function should calculate and return the sum of the 
    first n squares, where n >= 0. Assume that 1 is the first 
    square.
    
    For example, if n is 5, then the sum would be:

    1 + 4 + 9 + 16 + 25 = 55
   
    FOOD FOR THOUGHT:
    How much code from your solution to the previous question
    can be reused? Work smart. It's not plagiarism if it's your
    own code you wrote previously!

    '''
    sum = 0
    for i in range(n+1):
        sum += i ** 2
    return sum


# --------------------------------------------------------------
# 8) Summing Odd Digits
# --------------------------------------------------------------   
def odddigitsum(num):
    
    '''
    This function should calculate and return the sum of the 
    odd digits in the input integer num. The input can be any 
    integer, positive or negative.
    
    For example, if num is 482376, then the sum would be:
    
    3 + 7 = 10
    
    FOOD FOR THOUGHT:
    One thing that sets computer scientists apart from 
    mathematicians is our appreciation for the integer 
    division (//) and remainder (%) operations. Why do I 
    bring this up here of all places...? 
    
    '''
    sum = 0
    num_str = str(abs(num))
    for char in num_str:
        digit = int(char)
        if digit % 2 != 0:
            sum += digit
    return sum  
    
    
# --------------------------------------------------------------
# 9) Listing Exponentials
# --------------------------------------------------------------
def listexponential(n, base):
    
    '''
    This function should calculate and return a list containing
    the first n exponentials, where 'base' is the base. Assume 
    that 0 is the first exponent.
    
    For example, if n is 6, and base is 2, then the list would be:
    
    [ 2**0, 2**1, 2**2, 2**3, 2**4, 2**5 ] = [ 1, 2, 4, 8, 16, 32]

    FOOD FOR THOUGHT:
    Use your solution to answer the age old thought experiment:
    Would you rather have $1,000,000 now, or $0.01 doubled
    every day for a month? 
   
    '''
    list = []
    for i in range(n):
        list.append(base ** i)
    return list
    
    
# --------------------------------------------------------------
# 10) Concatenating Digits
# --------------------------------------------------------------      
def digitcat(s):
    
    '''
    This function accepts a string 's' as input, extracts the
    digit characters, and returns those digits as an integer.
    
    For example, if 's' is the string: 
    
    'I want 3 oranges, 24 bananas, and 101 dalmations'
    
    Then the function should return the integer 324101
    
    If there are no digits, return None.

    '''
    result = ""
    for char in s:
        if char.isdigit():
            result += char
    if result:
        return int(result)
    else:
        return None
    
# --------------------------------------------------------------
# 11) Parsing Floats
# --------------------------------------------------------------      
def stringtofloatlist(fltstr):
    
    '''
    Given an input string guaranteed to contain comma-separated
    floating point numbers, extract each float and place them
    in a list. Return the list.
    
    For example, if the input string is "1.23,2.4,3.123", then
    you should return the list [ 1.23, 2.4, 3.123 ]
    
    FOOD FOR THOUGHT:
    Don't reinvent the wheel. Familiarize yourself with the 
    Python documentation. Perhaps there are some built-in string 
    methods (*cough* split() *cough*) that could be of service?
    https://docs.python.org/3/library/stdtypes.html#string-methods
    Alternatively, DO reinvent the wheel, it's great practice
    either way!
    
    '''
    list = []
    split = fltstr.split(',')
    for i in split:
            list.append(float(i))
    return list


    
# --------------------------------------------------------------
# 12) Maximum of Each Type
# --------------------------------------------------------------      
def maxbytype(items):
    
    '''
    Assume that parameter 'items' is a heterogeneous list that
    may contain integers, floats, strings, and any other type.
    
    You should return a 3-tuple, where the first element is the
    largest integer, the second element is the largest float, 
    and the third element is the largest string.
    
    If any of the types are not found in the list at all, there
    can logically be no maximum, and therefore you should use 
    the value None to represent this.
    
    Example #1) if the input list is:
    [ "hello", 1, 3.14, 99, "cat", "tac", 2.7, "bat" ]
    Then the tuple returned should be: (99, 3.14, "tac")
    
    Example #2) if the input list is: 
    [ "hello", 1, 99, "cat", "tac", "bat" ]
    Then the tuple returned should be: (99, None, "tac")
    
    You can check the type of any object in Python by using the
    type() function. For example, type(item) == float, will 
    return True if item is a float, False otherwise.
    
    FOOD FOR THOUGHT:
    Why might we use the special value 'None' when there is no
    instance of a particular type present in the list? Why not
    use some error value, eg. -1 for integers, or the empty
    string if there is no string?

    '''
    max_int = None
    max_float = None
    max_str = None

    for item in items:
        if isinstance(item, int):
            if max_int is None or item > max_int:
                max_int = item
        elif isinstance(item, float):
            if max_float is None or item > max_float:
                max_float = item
        elif isinstance(item, str):
            if max_str is None or item > max_str:
                max_str = item

    return (max_int, max_float, max_str)
        
