temperatures = [73,74,75,71,69,72,76,73]
answer = []
l = [temperatures[0]]
h ={temperatures[0]:0}
stack = []

# loop stuff
i = 1
last = len(temperatures)-1

while i <= last:
    print(l)
    if temperatures[i] - l[-1] > 0:
        answer.append(i - h[l[-1]])
        l.append(temperatures[i])
        h[l[-1]] = i
        i += 1
        if len(stack)> 1:
            l.pop()
            while len(stack) > 1:
                stack.pop()
                i -= 1
            l.append(temperatures[i-1])
            h[l[-1]] = i-1
    else: 
        stack.append(temperatures[i])
        i += 1
# while len(answer) < len(temperatures):
#     answer.append(0)
print(answer)
print(stack)