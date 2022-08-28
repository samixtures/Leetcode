class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operator_set = {"+", "-", "*", "/"}
        stack = []
        total = 0
        if len(tokens) == 1:
            return tokens[0]
        for i, x in enumerate(tokens):
            if x not in operator_set:
                stack.append(x)
            elif x in operator_set:
                if x == "+":
                    total = 0
                    print(total)
                    print(stack)
                    total += int(stack[-1]) + int(stack[-2])
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(total)
                elif x == "-":
                    total = 0
                    print(total)
                    print(stack)
                    total += int(stack[-2]) - int(stack[-1])
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(total)
                elif x == "*":
                    total = 0
                    print(total)
                    print(stack)
                    total += int(float(stack[-1]) * float(stack[-2]))
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(total)
                elif x == "/":
                    total = 0
                    print(total)
                    print(stack)
                    print(x)
                    total += int(float(stack[-2]) / float(stack[-1]))
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(total)

        print("total is", total)
        return total