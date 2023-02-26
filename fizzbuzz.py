num = int(input("Enter a number"))



def fizzbuzz(num):
    while(num!=0):
        if(num%3==0 and num%5==0):
            print("fizzbuzz")
        elif(num%3==0):
            print("fizz")    
        elif(num%5==0):
            print("buzz")
        else:
            print(num)  
            
        num-=1      

fizzbuzz(num)        