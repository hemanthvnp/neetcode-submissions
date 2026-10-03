class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in tokens:
            
            match(i):
                case '+':
                    stack.append(stack.pop() + stack.pop()) 
                case '-':
                    stack.append(- stack.pop() + stack.pop())
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    stack.append(int ((1/(stack.pop()) * stack.pop())))
                case _ :
                    stack.append(int(i))
        return stack[0]
