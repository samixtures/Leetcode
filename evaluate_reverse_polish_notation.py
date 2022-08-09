tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

st = []
ret = 0
for x in tokens:
    if x != "+" and x != "-" and x != "*" and x != "/":
        st.append(x)
    else:
        temp1 = st[-1]
        temp2 = st[-2]
        st.pop(-1)
        st.pop(-2)
        if x == "+":
            ret += temp1 + temp2
        elif x == "-":
            ret += temp1 - temp2
        elif x == "*":
            ret = temp1 * temp2
        elif x == "/":
            ret += temp1//temp2
            
print(ret)
print(st)