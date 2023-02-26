def maxNumber(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print( num1, "is bigest number")
    if(num2>num1 and num2>num3):
        print( num2 ,"is bigest number")
    if(num3>num1 and num3>num2):
        print( num3 ,"is bigest number")
    return
maxNumber(10,21,3)


def addNumber(*nums):
    result=sum(nums)
    return result
print(addNumber(2,5,10))


def returnAge(name1,age):
    if(age<18):
        print("the Patient " , name1 , " is ", age , " and is underage ")
    else:
        print("the Patient " , name1 , " is " , age )



# returnAge("mori",17)
a = [9, 8, 10, 15, 11, 12, 14, 13,7]
def returnBiherThanTen() : 
    for x in a:
        if(x>=10):
          print(x)


returnBiherThanTen() 


def reverseString(x):
    return x[::-1]

print(reverseString("morteza"))


#6
x=lambda a,b:a/b
print(int(x(15,5)))

#7

def returnNumberA(x):
    index=0
    for y in x:
        if (y=="a"):
            index=index+1
    
    print("The number of iterations of letter a is:" , index)

returnNumberA("write a program that will count the number of letters")


