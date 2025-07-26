# Decorator to log every call
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Closure: A factory that returns a callback with state
def make_stateful_callback():
    count = 0
    @log_call  # Decorator applied to callback
    def callback(x):
        nonlocal count
        count += 1
        print(f"[CALLBACK] Processing {x}, total calls = {count}")
    return callback

# A generic processor that takes a callback
def process_data(data_list, callback):
    for item in data_list:
        callback(item)

# Use everything together
stateful_cb = make_stateful_callback()
process_data(["apple", "banana", "cherry"], stateful_cb)
