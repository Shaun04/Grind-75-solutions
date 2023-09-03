class Solution:
    def evalRPN(self, tokens: str) -> int:
        stack = []
        op = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                if len(stack) == 1:
                    return stack                
                x, y = stack.pop(), stack.pop()
                if i == "+":
                    ans = y + x
                elif i == "-":
                    ans = y - x
                elif i == "*":
                    ans = x * y
                else:
                    ans = y / x

                stack.append(int(ans))
        return stack[0]