dir = input("Enter l for left and r for right : ")
if(dir == 'l') :
    print("You are dead")
else : 
    dir = input("Enter l for left and r for right : ")
    if(dir == 'l') :
        print("You are dead")
    else :
        dir = input("Enter l for left and r for right : ")
        if(dir == 'r') :
            print("Malli madarchod")
        else : 
            print("You found the treasure")