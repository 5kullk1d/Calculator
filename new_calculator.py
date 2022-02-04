# function for operations
def operation (x,y,z):
    if y=='+':
        return x+z
    if y=='-':
        return x-z
    if y=='*':
        return x*z
    if y=='/':
        return x/z

equation=input('enter your equation: ')

eq=[]

# Function to add space between characters for data engineering
def add_spaces(equation):
    # -1 because we add 1 to i later on so need to stay in range
    for i in range(len(equation)-1):
        if equation[i].isnumeric() and equation[i+1].isnumeric() == False and equation[i+1] != ' ' and equation[i] != ' ':
            equation=equation[0:i+1]+' '+equation[i+1:]
            #add space
            return equation
        elif equation[i].isnumeric() == False and equation[i+1].isnumeric() and equation[i+1] != ' ' and equation[i] != ' ':
            #add space
            equation=equation[0:i+1]+' '+equation[i+1:]
            return equation
        elif equation[i].isnumeric() == False and equation[i+1].isnumeric() == False and equation[i+1] != ' ' and equation[i] != ' ':
            #add space
            equation=equation[0:i+1]+' '+equation[i+1:]
            return equation
    return equation

for i in range(len(equation)):
    equation = add_spaces(equation)

# Transfer string to list
eq=equation.split(' ')


# Change numeric characters to ints
eq_new = []
for i in eq:
    if i.isnumeric():
        eq_new.append(int(i))
    else:
        eq_new.append(i)

eq = eq_new

# Divide/ Multiply 
def multiply_divide(eq):
        for i in range(len(eq)):
            if eq[i]=='*' or eq[i]=='/' and eq[i+1] != '(' and eq[i-1] != ')':
                #take operation in list and replace with answer
                ans = operation(eq[i-1],eq[i],eq[i+1])
                eq.pop(i-1)
                eq.pop(i-1)
                eq[i-1]= ans
                return True
        return False

# Add/ Subtract
def add_subtract(eq):
        for i in range(len(eq)):
            if eq[i]=='+' or eq[i]=='-' and eq[i+1] != '(' and eq[i-1] != ')':
                #take operation in list and replace with answer
                ans = operation(eq[i-1],eq[i],eq[i+1])
                eq.pop(i-1)
                eq.pop(i-1)
                eq[i-1]= ans
                return True
        return False

# Multiply/ Divide in Brackets
def multiply_divide_bracket(eq, i):
    #take operation in list and replace with answer
    ans = operation(eq[i-1],eq[i],eq[i+1])
    eq.pop(i-1)
    eq.pop(i-1)
    eq[i-1]= ans
    return eq

# Add/ Subtract in Brackets
def add_subtract_bracket(eq,i):
    #take operation in list and replace with answer
    ans = operation(eq[i-1],eq[i],eq[i+1])
    eq.pop(i-1)
    eq.pop(i-1)
    eq[i-1]= ans
    return eq

# Look for operators in brackets
def brackets(eq,i,a):
    m =(eq[i+1:a])    
    while len(m) > 1:
        for i in range(len(m)):
            if m[i] == '*' or m[i] == '/':
                m = multiply_divide_bracket(m, i)
                break
        for i in range(len(m)):
            if m[i]=='+' or m[i]=='-':
                m = add_subtract_bracket(m,i)
                break
    return m
        


# Look for brackets
def brackets2(eq):
    for i in range(len(eq)):
        if eq[i] == '(':
            for a in range(len(eq)):
                if eq[a] == ')':
                    eq=eq[0:i]+brackets(eq,i,a)+eq[a+1:]
                    return eq
    return False



while brackets2(eq)!=False:
    eq = brackets2(eq)

#repeats until multiplication/division is done
while multiply_divide(eq):
    y=0
#repeats until addition/subtraction is done
while add_subtract(eq):
    y=0
print(eq)
