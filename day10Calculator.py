def calc():
    num1 = float(input("What's the first number ? : "))

    print("+\n-\n*\n/\n ")

    t = True
    while t:
        operator = input("Pick an operator ? : ")
        num2 = float(input("What's the next number ? : "))

        def cal(a, b, o):
            if o == "+":
                return num1 + num2
            elif o == "-":
                return num1 - num2
            elif o == "*":
                return num1 * num2
            elif o == "/":
                return num1 / num2
            else:
                return 0

        answer = cal(num1, num2, operator)
        print(f"{num1}{operator}{num2} = {answer}")
        to_continue = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation")
        if to_continue == "y":
            num1 = answer
        else:
            t = False
            calc()


calc()

