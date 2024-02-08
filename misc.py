def something(*args, **kwargs):
    
    def some_else(*args, **kwargs):
        return args 
    
    return some_else(kwargs)

print(something(8,10,6,a=1, b=2, c=3))