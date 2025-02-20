# Kan du se det her
#Define a function to solve a function of form x^y=z for x
def myfunc(y,z):
    x = z**(1/y)
    return(x)
    
print(myfunc(3,5))
