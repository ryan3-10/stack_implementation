from stack import Stack

def eval_postfix(expr):
    if not isinstance(expr, str):
        raise ValueError("Expression must be a string")
    
    valid_characters = "123456789+-*/ "
    
    for char in expr:
        if char not in valid_characters:
            raise SyntaxError("Expressions must contain numbers and operators only")
        
    stack1 = Stack()

    for char in expr:
        if char.isnumeric():
            stack1.push(char)
        
        elif char != " ":           # Character is an operator
            operator = char
            try:
                op1 = stack1.pop()
                op2 = stack1.pop()
            except:
                raise SyntaxError("Invalid postfix expreesion")
            
            result = eval(f"{op2} {operator} {op1}")
            stack1.push(result)
    
    try:
        result = float(stack1.pop())
    except:
        raise SyntaxError("Invalid postfix expression")
    
    return result      

def equal_or_higher_precedence(op1, op2):
    if op1 not in ["*", "/", "-", "+"] or op2 not in ["*", "/", "-", "+"]:
        raise ValueError("Both arguments must be operators to determine precedence")
    
    if op1 == "*" or op1 == "/":
        return True
    
    return op2 == "+" or op2 == "-"

def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError("Expression must be a string")
    
    valid_characters = "123456789+-*/()  "

    for char in expr:
        if char not in valid_characters:
            raise SyntaxError("Expressions must contain numbers, parantheses, and operators only")
    
    operators = ["*", "/", "-", "+"]
    stack1 = Stack()
    output = ""

    for char in expr:
        try:
            if char == "(":
                stack1.push(char)
            
            elif char.isnumeric():
                output += char + " "
            
            elif char in operators:
                while (stack1.size() > 0 and stack1.top() in operators and 
                equal_or_higher_precedence(stack1.top(), char)):
                    if stack1.top() in operators:
                        output += stack1.pop() + " "
                    
                    else:
                        output += stack1.pop() + " "
                        
                stack1.push(char)
            
            elif char == ")":
                output += stack1.pop() + " "
                
                while stack1.top() != "(":
                    if stack1.top() in operators:
                        output += stack1.pop() + " "
                        
                    else:
                        output += stack1.pop() + " "
                        
                stack1.pop()
        
        except:
            raise SyntaxError("Invalid infix expression")
            
    while stack1.size() > 0:
        output += stack1.pop() + " "
    
    return output

def main():
    with open("data.txt", "r") as input:
        for line in input:
            infix = line.strip()    # Remove newline character
            postfix = in2post(infix)
            answer = eval_postfix(postfix)

            print(f"infix: {infix}")
            print(f"postfix: {postfix}")
            print(f"answer: {answer}")
            print("\n")
    
    print(in2post("(8+3)*(5-6))"))

if __name__=="__main__":
    main()