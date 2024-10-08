'''
    LEGB (Local, Enclosing, Global, Built-in)
    # Local variable defined with in the function.
    # Enclosing - variable in local scope enclosing functions
    # Global - Global defined at the top level of module and explicitly declared 
    # Built-in preassigned variable in python.
    
    python check if any variable declared
    whether it's Local scope elif Enclosing Scope elif Global scope else Built-in scope.
    
'''
import builtins

print(dir(builtins))

x = 'global x'

def test(z):
    
    #global x
    x = 'local x'
    y = 'local y'     
    #print(y)      # python checks y is in local scope if it's find print local variable
    print(x)       # python checks x is in local scope if x not find in local local later it check x in enclosing scope or not. if not present check in global scope.
    print(z)
    
test("local z")
print(x)
# print(y)

m = min([5, 1, 4, 2, 3])
print(m)

# Enclosing Scope
x = 'global x'
def outer():
    
    x = 'Outer X'
    
    def inner():
        
        #nonlocal x
        x = 'inner x'   # nonlocal is used more often when compared to global
        # nonlocal is can be useful in order to change the state of closers and decorators 
        print(x) # now x is enclosing scope 
        
    inner()
    print(x)

outer()
print(x)
