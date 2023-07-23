n1 = 409
# num1 = int(input("Enter any one number: "))
# prime number is greater than 1
if n1 > 1:
# check the following factors
    m =''
    for x in range (2,n1):
        if (n1 % x) == 0:
            print(n1,"is not a prime number")
            print(x,"times",n1//x,"is",n1)
            break
        else:
            m ="is a prime number"
    print(m)
# if input number is smaller than
# or equal to the value 1, then it is not prime number
else:
    print(n1,"is not a prime number")