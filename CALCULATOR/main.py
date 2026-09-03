try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform. Press + for addition\n - for subtraction\n * for multiplication\n / for division")

    o = input("Enter the operation: ")
    match o:
        case "+":
           print(f"The result is: {a + b}")
        case "-":
           print(f"The result is: {a - b}")
        case "*":
           print(f"The result is: {a * b}")
        case "/":
           print(f"The result is: {a / b}")
        case default:
           print(f"There was an error")

except Exception as e:
   print("Enter avalid value of a and b")           