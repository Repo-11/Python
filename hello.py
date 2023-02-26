friends = ["ram" , "shyam", "raju", "vinit", "kalu", "rina"]

import random
num = random.randint(0,5)
def whowillpay(num):
    print(f"Today's bill will be paid by : {friends[num]}")
    
whowillpay(num)    

