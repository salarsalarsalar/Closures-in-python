""" 
Python LEGB Rule
Local, Enclosing, Global, Built-in
"""
# If all are commented out, the code will print built-in max function

# max = "I was defined in the global scope"
def outer_function():
    # max="Hi, I'm in the outer function"
    # print(max) # will print the local variable
    def inner_function():
        # max = "Hello, I'm in the inner function"
        print(max) 

    # inner_function is called within outer_function
    inner_function()

outer_function()

""" 
Scope of a name defines the area of a program
in which a name can be accessed.
python looks for names in the following scope order:
1. Local scope: Names defined within the current function.
2. Enclosing scope: Names defined in the enclosing function (if any).
3. Global scope: Names defined at the top level of the module.
4. Built-in scope: Names pre-defined by Python (like `max`, `print`, etc.).
"""