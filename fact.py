def fact(num):
    factor = 1
    # for i in range(1,num+1):
    #     factor *= i
    for i in range(num,1,-1):
        factor *= i
    print(f"Factorial of {num} is {factor}")
    
fact(6)