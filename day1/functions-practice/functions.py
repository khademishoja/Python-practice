# Write a function with one `number` argument that returns double the argument
def double(number: int):
    return 2 * number

# Write a function with two `number` arguments that returns double the first argument
def double_first(number1: int, number2: int):
    return number1 * 2

# Write a function with two `number` arguments that returns double the largest argument
def big_double(number1: int, number2: int):
    if(number1>number2):
        return number1 *2
    if (number2>number1):
        return number2*2
    else:
        return "they are equal"

# Write a function with a `string` argument and a `number` argument that repeates the string from the first argument but repeated the amount of times equal to the second argument. If the second number is negative, return an empty string
def repeat(text: str, number: int):

    if(number>0):
        # for number in text:
            return text * number
    if(number<0):
        return ""
# print(repeat("mori",3))

    # pass

# Write a function without any arguments. Have it return the string `'na'` repeated 10 times followed by the string `' batman!'`. Use the `repeat` function you used before to accomplish this
def batman():
    txt="na"
    bat=repeat(txt,10)
    return bat+ " batman!"
# print(batman())



# Write a function with two `number` arguments. Have it return the largest number of the two
def max(number1: int, number2: int):
    if (number1>number2):
        return number1
    if (number2>number1):
        return number2
    # pass

# Write a function with two `number` arguments. Have it return the smallest number of the two divided by the largest number
def max_divide(number1: int, number2: int):
    if (number1<number2):
        return number1/number2
    if (number2<number1):
        return number2/number1

# Write a function with two `string` arguments. Have it return the longest string
def max_string(string1: str, string2: str):
    if(len(string1)>len(string2)):
        return string1
    if(len(string2)>len(string1)):
        return string2
    else:
        return string1

# Write a function with a single `number` argument. Return a boolean that indicated wether this number is even
def even(number: int):
    if(number%2==0):
        return True
    else:
        return False

# Write a function with a single `number` argument. Return a list of all the positive numbers lower than this argument that are even
def even_below(number: int):
    y=[]

    if(number>0):
        x=0
        for x in range (number):
            if(x%2==0):
                y.append(x)
                
        return y
    else:
        return []
# print(even_below(10))
    

# Write a function with a single `list of numbers` argument. Return a list of all the numbers in this list that are even
def even_in(numbers: list[int]):
    x=len(numbers)
    y=[]
    for x in numbers:
        if(x%2==0):
            y.append(x)
    return y

# Write a function with a single `list of numbers` argument. Return the result of multiplying all the numbers. If the input contains just 1 number, return that number
def multiply_list(numbers: list[int]):
    # y=0
    # while y>len(numbers):
    #     mult=numbers[y]*numbers[y+1]
    #     y=y+1
    # return mult
    p=1
    for num in numbers:
        p=p*num
    return p
        

# Write a function with a single `list of numbers` argument. Return the result of dividing the number from left to right. So the first number gets divided by the second and the result of that gets divided by the third (and so on..). If the list contains a zero, return zero. If the list contains just one number, return that number
def divide_array(numbers: list[int]):
    if len(numbers) == 1:
        return numbers[0]
    if 0 in numbers:
        return 0
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result= result/ numbers[i]
        return result

    # pass

# Write a functions that takes a list of numbers and an argument. Return the average of those numbers
def average(numbers: list[int]):
    a=sum(numbers)/len(numbers)
    return a
    
