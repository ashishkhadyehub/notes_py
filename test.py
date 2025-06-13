def make_multiplier(n):
    def innerfunc(x):
        return x*n
    return innerfunc

funccall=make_multiplier(3)
print(funccall(10))