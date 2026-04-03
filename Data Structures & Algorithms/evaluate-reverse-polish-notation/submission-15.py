class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])

        stack = []
        
        print(stack)
        for i in range(len(tokens)):
            if tokens[i] in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                #evalueate
                match tokens[i]:
                    case "+":
                        stack.append(str(num1 + num2))
                    case "*":
                        stack.append(str(num1 * num2))
                    case "-":
                        stack.append(str(num1 - num2))
                    case "/":
                        stack.append(str(int(num1 / num2)))
            else:
                stack.append(tokens[i])

            print(stack)
        return int(stack[0])
                    
            
        