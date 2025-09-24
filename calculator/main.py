import inputmodule
import logicmodule

while True:
    num1 = inputmodule.getNum1()
    num2 = inputmodule.getNum2()
    op = inputmodule.getOperation()

    result = logicmodule.checkOp(op, num1, num2)
    print("Result:", result)

    # Ask if user wants to continue
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        break
