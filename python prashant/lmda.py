num1 = 3
multiply=num1*num1
print("your squared number is ",multiply)




def square(a):
    square=a*a
    print("your square number is ",square)
square(20)



lmd = lambda a: a*a
print("your square is",lmd(10))


lmd = lambda a:a+a
print("your addition is", lmd(3))


lmd = lambda a: a-a
print ("your subtraction is ",lmd(5))


lmd = lambda a:a/a
print ("your division is ",lmd(10))


num = [1,2,3,4]
sqr= list(map(lambda a:a**2,num))
print (sqr)
