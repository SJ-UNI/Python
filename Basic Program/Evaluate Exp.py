operands=set(['+','-','*','/','^','(',')'])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
exp=input("Enter infix Expression:")
def inf(exp):
    stack=[]
    opbox=""
    for i in exp:
        if i  not in operands:
            opbox+=i
        elif i=="(":
            stack.append(i)
        elif i==")":
            while stack and stack[-1]!="(":
                opbox+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and priority[i]<=priority[stack[-1]]:
                opbox+=stack.pop()
            stack.append(i)
    while stack:
        opbox += stack.pop()
    return opbox
pf=inf(exp)
pfl=[]
for i in pf:
    pfl.append(i)
    pfl.append(" ")
pfl.pop()
y=""
for i in pfl:
    x=i
    y=y+x
print("INFIX EXPRESSION:",exp)
print("POSTFIX EXPRESSION:",y)
operand=['+','-','*','/','^']
stack=[]
ex=y
exp=ex.split(' ')
for i in exp:
    if i not in operand:
        stack.append(i)
    else:
        a=stack.pop()
        b=stack.pop()
        if i=='+':
            ans = float(a)+float(b)
        elif i=='-':
            ans = float(a)-float(b)
        elif i=='*':
            ans = float(a)*float(b)
        elif i=='/':
            ans = float(a)/float(b)
        elif i=='^':
            ans = float(a)**float(b)
        stack.append(str(ans))
print("ans=",stack[0])
