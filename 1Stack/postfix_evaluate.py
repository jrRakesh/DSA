while True:
    stack = []
    expression = input("Enter the postfix expression : ")
    characters = expression.split()
    for char in characters:
        if( char == "+"):
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 + val1
            stack.append(result)
        elif( char == "-"):
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 - val1
            stack.append(result)
        elif( char == "*"):
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 * val1
            stack.append(result)
        elif( char == "/"):
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 / val1
            stack.append(result)
        elif( char == "^" or char == "$"):
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 ** val1
            stack.append(result)
        else:
            operand = int(char)
            stack.append(operand)
    print(f"The result is {stack[0]}")
