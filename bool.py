def iseven(x):
    return True if x%2==0 else False

num = int(input("Enter : "))
if iseven(num):
    print("Even")
else:
    print("Odd")