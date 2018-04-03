# function-composition-py
Function composition method in python. This is an example when the reduce operation in python is preferred over an iterative approach.

## Description
The python function accepts a list of lambda functions as the functions argument.  
The first function in the list is the innermost function, which is then the input the the next function in the list, and so on. For example:
def function_composition(x)
    output1 = f1(x)
    output2 = f2(output1) = f2(f1(x))
    output3 = f3(output2) = f3(f2(f1(x)))
    ...
    outputN = fN(outputN-1) = fN(fN-1(...(f3(f2(f1(x))))))
    return outputN

x = [f1(x), f2(x), f3(x), ..., fN(x)]

For example:  
f(x) = x + 3  
g(x) = x^2  
Then the return of function_composition is:  
h(x) = g(f(x)) = (x+3)^2  
If x = 4, then h(x=4) = 49.  
