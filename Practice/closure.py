""" 
record = [] # this is in global which can be problematic
def print_(data):
    # you cant do this
    # because everytime a new record is created
    # it will overwrite the previous one  
    # record = []  
    print(data)
    record.append(data) 
    """


# for this we create a closure
""" 
def print_with_memory():
    record = [] 
    # this right now doesnt exist in global scope
    # so it will give name error
    def print_(data):
        print(data)
        record.append(data)
"""

""" 
def print_with_memory():
    # nonlocal record # nonlocal only works in nested functions
    record = [] 
    # this right now doesnt exist in global scope
    # so it will give name error
    def inner(data):
        print(data)
        record.append(data)
        # print(record)
    return inner

print_ = print_with_memory()

print_("Real Python")
print_("I love Python")

# Print_ contains a reference to the record list
# This can be viewed by checking the closure
print(print_.__closure__) 
print(print_.__closure__[0].cell_contents) 
# print(record)

 """

def print_with_memory():
    record = []
    
    def inner(data):
        print(data)
        record.append(data)

    inner.record = record  # Attach record as an attribute
    return inner

printer = print_with_memory()
printer("hello")
printer("world")

print("Record:", printer.record)
