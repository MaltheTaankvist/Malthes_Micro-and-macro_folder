
#Define a function to solve a function with Newton Rhapson
def f(x):
    return x**3 - 5

def df(x):
    return 3*x**2

# Newton-Raphson method
def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        x = x - (fx / dfx)
    return x

# Initial guess
x0 = 1.5
root = newton_raphson(x0)

print("Root:", root)
