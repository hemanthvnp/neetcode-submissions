
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                op1 = s.pop()
                op2 = s.pop()

                if token == "+":
                    s.append(op2 + op1)
                elif token == "-":
                    s.append(op2 - op1)
                elif token == "*":
                    s.append(op2 * op1)
                else:
                    s.append(int(op2 / op1))
            else:
                s.append(int(token))

        return s[-1]