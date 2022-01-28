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
    return equation

for i in range(len(equation)):
    equation = add_spaces(equation)

print("Please almighty, let this be right. Equation is equal to: ", equation)

eq=equation.split(' ')
print(eq, " before")

eq_new = []
for i in eq:
    if i.isnumeric():
        eq_new.append(int(i))
    else:
        eq_new.append(i)

eq = eq_new
print(eq, " after")

# Convert input string to list 
#for i in range(len(equation)):
#    if equation[i].isnumeric() and equation[i+1].isnumeric() == False:
#        eq.append(int(equation[i]))
#    elif 
#    else:
#        eq.append(equation[i])

def multiply_divide(eq):
        for i in range(len(eq)):
            if eq[i]=='*' or eq[i]=='/':
                #take operation in list and replace with answer
                ans = operation(eq[i-1],eq[i],eq[i+1])
                eq.pop(i-1)
                eq.pop(i-1)
                eq[i-1]= ans
                return True
        return False

def add_subtract(eq):
        for i in range(len(eq)):
            if eq[i]=='+' or eq[i]=='-':
                #take operation in list and replace with answer
                ans = operation(eq[i-1],eq[i],eq[i+1])
                eq.pop(i-1)
                eq.pop(i-1)
                eq[i-1]= ans
                print("We have entered add_subtract")
                return True
        return False

#repeats until multiplication/division is done
while multiply_divide(eq):
    y=0
#repeats until addition/subtraction is done
while add_subtract(eq):
    y=0

print(eq)
